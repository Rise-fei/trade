from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import re
import requests
import time,datetime
from user.models import CustLoginRecord


class LoginCheckMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # print(request.session.get('is_login'))
        print(request.path_info)
        print(request.path)
        # 如果请求url在白名单内，说明该请求不必登录就可用！
        white_url = ['/logout_all_cuser/','/search/yellow/','/send_mail_extend/','/check_status/','/login/','/login_check/','/admin/','/static/','/logout/','/offline/','^$']
        for re_url in white_url:
            if re.match(re_url,request.path):
                print('路径匹配成功')
                return


        # print('路径匹配不成功')
        # 否则，判断登录状态
        if request.session.get('is_login'):
            session_key = request.COOKIES.get('session_key')
            if session_key:
                # 如果oa管理员通过一键下线当前客户所有终端，那么此web项目目前是不知道的，所以向主服务器发送请求查询一下
                # 但是此方法不好，该每次发送请求，都要向主服务器查询，最好改成：
                # ****（主服务器执行一键下线后，给当前web项目发送请求，告知当前项目哪一个客户下线了，在此web项目中加以判断，后续优化！！）
                # print(1)
                url = 'http://www.sstrade.net:8888/ssapi/query_is_login?session_key=%s' % session_key
                print(url)
                res = requests.get(url)
                # print(2)
                if res.content.decode() == 'yes':
                    print('当前浏览器中存储的用户cookie：session_key在服务器端有对应的记录，即该用户是登录状态！')
                    record = CustLoginRecord.objects.filter(oa_session_key=session_key)
                    if record:
                        print(record[0].oa_session_key)
                        record[0].login_time = datetime.datetime.fromtimestamp(time.time())
                        record[0].save()
                    return
                else:
                    print('当前浏览器中存储的用户cookie：session_key在服务器端没有对应的记录，即该用户应该下线！')
                    request.session['is_login'] = False
                    request.COOKIES['session_key'] = ""
                    return redirect('/login/')
            else:
                return redirect('/login/')

        else:
            return redirect('/login/')


