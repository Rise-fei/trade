from threading import Thread, enumerate as threading_enumerate
from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.conf import settings
from user.models import *
# from user import models as user_models
from django.core.mail import send_mail
import requests
import time
import json
import os
import random
from django.db import connections, connection


# Create your views here.
def test(request):
    if request.session.get('id_list'):
        print(request.session.get('id_list'))
        id_list = request.session.get('id_list')
    else:
        keyword = 'sofa'
        data_set = SearchResult.objects.all().filter(keyword__icontains=keyword).values_list('id')
        id_list = [i[0] for i in data_set]
        request.session["id_list"] = id_list

    return HttpResponse('ok')


def tree(request):
    #
    # ss = SearchResult.objects.update_or_create(defaults={
    #     'website': "1112", "addr": "12321","phone": "111","query_flag": "1123",
    # }, keyword = "aaab", company = "ceshi", )
    # print(ss)
    # user_obj = User.objects.get(id=1)
    # ret = user_obj.searchresult_set.add(ss[0].id)
    # print(ret)
    # 将全部的搜索结果 和 userid 映射
    # user = User.objects.get(id=userid)
    #
    # results = SearchResult.objects.all()
    # user.searchresult_set.add(*results)
    # print(len(results))

    # sr_list = SearchResult.objects.all()
    # index = 0
    # li = []
    # for i in sr_list:
    #     usr = UserSearchResult(user_id=1,searchresult=i)
    #     li.append(usr)
    #     index += 1
    #     print('添加成功',index)
    # print('************')
    # UserSearchResult.objects.bulk_create(li)
    # print('************')

    return render(request, 'tree/test.html')


def delete_user_keyword_map(user_id, keyword):
    user = User.objects.filter(id=user_id)[0]
    # print(user)
    objs = user.searchresult_set.all().filter(keyword=keyword)
    # print(objs)
    # print(len(objs))
    objs.delete()
    # print(len(objs))


def delete_keyword(request):
    kid = request.POST.get("kid")
    objs = SearchKey.objects.filter(id=kid)
    for obj in objs:
        user_id = obj.user_id
        keyword = obj.keyword
        delete_user_keyword_map(user_id, keyword)
    objs.delete()

    return JsonResponse({})


def delete_keywords(request):
    ids = request.POST.get("ids")
    ids = json.loads(ids)
    print(ids)
    objs = SearchKey.objects.filter(id__in=ids)
    for obj in objs:
        user_id = obj.user_id
        keyword = obj.keyword
        delete_user_keyword_map(user_id, keyword)
    objs.delete()
    return JsonResponse({})


def keyword_manage(request):
    userid = request.session.get('userid')
    keywords = SearchKey.objects.filter(user_id=userid)
    return render(request, 'keyword_manage.html', locals())


def delete_user_searchresult(request):
    userid = request.session.get('userid')
    id_list = request.POST.get("search_id_list")
    searchresult_id_list = json.loads(id_list)
    # 删除 user1 对应- sr idlist 的记录
    # sr_list = SearchResult.objects.filter(id__in=searchresult_id_list)
    # re1 = SearchResult.objects.all()
    # print(len(re1))
    # print((sr_list))
    # print(len(sr_list))
    user_obj = User.objects.get(id=userid)
    # user_obj.searchresult_set.all().filter(id__in=searchresult_id_list).delete()
    #
    user_obj.searchresult_set.remove(*searchresult_id_list)
    re1 = user_obj.searchresult_set.all()
    print(len(re1))

    return JsonResponse({})


def remote_ip(request):
    # print(request.META)
    print(request.META["HTTP_USER_AGENT"])
    # print(request.environ["HTTP_USER_AGENT"])
    # print(request.scheme)
    ip = request.META.get("REMOTE_ADDR")
    print(ip)
    return JsonResponse({
        'ip': ip,
    })


def index(request):
    ip = request.META.get("REMOTE_ADDR")
    print(ip)
    username = request.session.get('username')
    t = time.localtime()
    H = t.tm_hour
    if H >= 6 and H < 11:
        tt = 'Good morning'
    elif H >= 11 and H <= 18:
        tt = 'Good afternoon'
    else:
        tt = 'Good evening'
    print(t)

    tips1 = "%s !      %s. " % (tt, username)
    tips = ''
    # return render(request, 'index.html', {'tips': tips, 'tips1': tips1})
    return render(request, 'APP.html')

import datetime
def login(request):
    if request.session.get('is_login'):
        session_key = request.COOKIES.get('session_key')
        if session_key:
            # 如果oa管理员通过一键下线当前客户所有终端，那么此web项目目前是不知道的，所以向主服务器发送请求查询一下
            # 但是此方法不好，该每次发送请求，都要向主服务器查询，最好改成：
            # ****（主服务器执行一键下线后，给当前web项目发送请求，告知当前项目哪一个客户下线了，在此web项目中加以判断，后续优化！！）
            # print(1)
            url = 'http://www.sstrade.net:8080/ssapi/query_is_login?session_key=%s' % session_key
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
                return redirect('/index/')

    return render(request, 'login_log.html')


def login_check(request):
    '''
    登录校验：接收前端发送的ajax请求，接收账号密码，然后向oa服务器发送登录请求
    如果登录成功：
        那么将username,is_login（True）存入当前session中。并且将oa登录成功保存的sessionkey拿过来保存在当前cookie中。
        添加登录信息至custloginrecord表中。
        返回 ret 1
    如果login full，即登录终端到达授权数：
        返回 ret 0
    如果超出产品服务时间；
        返回 ret -1
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')
    product = settings.PRODUCT  # 后续改进
    version = settings.VERSION  # 后续改进
    print(username)
    print(password)
    url = 'http://www.sstrade.net:8080/ssapi/customerlogin/?username=%s&password=%s&product=%s&version=%s' % (
        username, password, product, version)
    url = 'http://www.sstrade.net:8888/ssapi/customerlogin/?username=%s&password=%s&product=%s&version=%s' % (
        username, password, product, version)
    print(url)
    res = requests.get(url)
    response_content = res.content.decode()
    print(response_content)
    if response_content == 'success':
        ret = {
            'status': 1,
            'msg': '登录成功',
        }
        # user = User.objects.update_or_create(defaults={
        #     "update_time":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
        # },username=username,password=password)

        query = User.objects.filter(username=username, password=password)
        if query:
            user = query[0]
            user.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            user.save()
        else:
            user = User.objects.create(username=username, password=password)

        print(request.user)
        request.user = user
        print(request.user)
        print(request.user.username)
        print(request.user.password)
        request.session['userid'] = user.id
        request.session['username'] = username
        print(res.cookies)
        request.session['is_login'] = True
        response = JsonResponse(ret)
        response.set_cookie('session_key', res.cookies.get('sessionid'))

        CustLoginRecord.objects.create(username=username, oa_session_key=res.cookies.get('sessionid'))
        # 用户账号密码正确后，在登录记录表中 添加记录，并且成功返回登录后的界面。
        # 接下来将表中超过授权数的 登录日期早的用户t下线。

        # 向oa系统发送请求，查询当前username对应的product授权数。
        url = 'http://www.sstrade.net:8080/ssapi/query_cust_auth_num?username=%s&product=%s' % (username, product)
        url = 'http://www.sstrade.net:8888/ssapi/query_cust_auth_num?username=%s&product=%s' % (username, product)
        res = requests.get(url).content.decode()
        authorization_num = int(res)
        if authorization_num == 0:
            print('当前用户和产品不匹配')
        else:
            cust_records = CustLoginRecord.objects.filter(username=username).order_by('-login_time')
            if len(cust_records) < authorization_num:
                pass
            else:
                # cust_records =cust_records.
                for cust in cust_records[authorization_num:]:
                    # 超出授权数，向oa系统发送请求清除当前sessionkey对应的session信息。
                    oa_session_key = cust.oa_session_key
                    url = 'http://www.sstrade.net:8080/ssapi/logoutaccount2?session_key=%s' % oa_session_key
                    url = 'http://www.sstrade.net:8888/ssapi/logoutaccount2?session_key=%s' % oa_session_key
                    res = requests.get(url)
                    response_content = res.content.decode()
                    print(response_content)
                    cust.delete()

    else:
        if response_content == 'login is full':
            ret = {
                'status': 0,
                'msg': '登录账号已到达最大授权数',
            }
        elif response_content == 'fail':
            ret = {
                'status': -1,
                'msg': '用户名或密码错误',
            }
        elif response_content == 'out of service time':
            ret = {
                'status': -1,
                'msg': '超出产品服务时间',
            }
        else:
            ret = {
                'status': -1,
                'msg': '服务器繁忙，请稍后重试！！！',
            }
        request.session['is_login'] = False
        request.session['userid'] = ""
        request.COOKIES['session_key'] = ""
        response = JsonResponse(ret)
    return response


def logout(request):
    session_key = request.COOKIES.get('session_key')
    print(session_key)
    request.COOKIES['session_key'] = ""
    request.session['is_login'] = False
    request.session['userid'] = ""

    # 还需要向trade项目发送注销请求，将服务器中存储该客户的session信息清除(将session_key 以参数的形式放入请求中去)！！！
    url = 'http://www.sstrade.net:8080/ssapi/logoutaccount2?session_key=%s' % session_key
    url = 'http://www.sstrade.net:8888/ssapi/logoutaccount2?session_key=%s' % session_key
    res = requests.get(url)
    response_content = res.content.decode()
    try:
        CustLoginRecord.objects.get(oa_session_key=session_key).delete()
    except:
        pass

    if response_content == 'delete ok':
        print('注销成功')

    else:
        print('向服务器发送删除session请求出错')
    return redirect('/login/')


def check():
    while True:
        time.sleep(10)
        login_records = CustLoginRecord.objects.all()
        if login_records:
            for record in login_records:
                last_active_time = record.login_time.timestamp()
                current_time = time.time()
                # 如果用户1.5个小时内没有活跃，那么将其t下线！
                if current_time - last_active_time > 5400:
                    print(record.username)
                    # 下线该用户
                    session_key = record.oa_session_key
                    url = 'http://www.sstrade.net:8080/ssapi/logoutaccount2?session_key=%s' % session_key
                    url = 'http://www.sstrade.net:8888/ssapi/logoutaccount2?session_key=%s' % session_key
                    res = requests.get(url)
                    response_content = res.content.decode()
                    try:
                        record.delete()
                    except:
                        pass


def check_status(request):
    thread_list = threading_enumerate()
    t_name_list = [t.name for t in thread_list]
    # print("***********")
    # print(t_name_list)
    # print("***********")
    if "check_trade" not in t_name_list:
        t = Thread(target=check)
        t.setName('check_trade')
        t.start()
        tips = "开启检测线程"
    else:
        tips = "检测线程已开启"
    return render(request, 'tips.html', {'tips': tips})


def offline(request):
    product = settings.PRODUCT  # 后续改进
    version = settings.VERSION  # 后续改进
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        # 向oa系统发送请求，查询当前username对应的product授权数,然后将授权数-1个账号信息保留，其他删除
        url = 'http://www.sstrade.net:8080/ssapi/query_cust_auth_num?username=%s&product=%s' % (username, product)
        url = 'http://www.sstrade.net:8888/ssapi/query_cust_auth_num?username=%s&product=%s' % (username, product)
        res = requests.get(url).content.decode()
        authorization_num = int(res)
        cust_records = CustLoginRecord.objects.filter(username=username).order_by('-login_time')

        if cust_records[authorization_num - 1]:
            for cust in cust_records[authorization_num - 1:]:
                # 超出授权数，向oa系统发送请求清除当前sessionkey对应的session信息。
                oa_session_key = cust.oa_session_key
                url = 'http://www.sstrade.net:8080/ssapi/logoutaccount2?session_key=%s' % oa_session_key
                url = 'http://www.sstrade.net:8888/ssapi/logoutaccount2?session_key=%s' % oa_session_key
                res = requests.get(url)
                response_content = res.content.decode()
                print(response_content)
                cust.delete()

            # # 将之前的最早登录的终端下线
            # cust = CustLoginRecord.objects.filter(username=username).order_by('login_time').first()
            # oa_session_key = cust.oa_session_key
            # url = 'http://www.sstrade.net:8080/ssapi/logoutaccount2?session_key=%s' % oa_session_key
            # res = requests.get(url)
            # response_content = res.content.decode()
            # print(response_content)
            # cust.delete()

            ret = {
                'code': 1
            }

            # 然后再登录当前账号
            url2 = 'http://www.sstrade.net:8080/ssapi/customerlogin/?username=%s&password=%s&product=%s&version=%s' % (
                username, password, product, version)
            url2 = 'http://www.sstrade.net:8888/ssapi/customerlogin/?username=%s&password=%s&product=%s&version=%s' % (
                username, password, product, version)
            res2 = requests.get(url2)
            response_content2 = res2.content.decode()
            print('*******************')
            print(response_content2)
            print('*******************')
            query = User.objects.filter(username=username, password=password)
            if query:
                user = query[0]
                user.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                user.save()
            else:
                user = User.objects.create(username=username, password=password)

            request.session['userid'] = user.id
            request.session['username'] = username
            print(res2.cookies)
            request.session['is_login'] = True
            response = JsonResponse(ret)
            response.set_cookie('session_key', res2.cookies.get('sessionid'))
            CustLoginRecord.objects.create(username=username, oa_session_key=res2.cookies.get('sessionid'))
        else:
            ret = {
                'code': 0,
                'username': username,
            }
            response = JsonResponse(ret)
    except:
        ret = {
            'code': 0,
            'username': username,
        }
        response = JsonResponse(ret)
    return response


# 待完善，注销当前用户的所有终端！！！慎用！！
def logout_all_cuser(request):
    cname = request.GET.get('username')
    productid = settings.PRODUCT
    url = 'http://www.sstrade.net:8888/ssapi/logout_cuser_all?productid=' + str(productid) + '&cusername=' + cname
    print(url)
    res = requests.get(url)
    print(res)
    return JsonResponse({})


def delete_email(request):
    userid = request.session.get('userid')
    ids = request.POST.get('senderid')
    id_list = json.loads(ids)
    ret = Sender.objects.filter(id__in=id_list)
    for sender in ret:
        if sender.user.id == userid:
            sender.delete()
    return JsonResponse({})


def delete_letter(request):
    userid = request.session.get('userid')
    ids = request.POST.get('letter_ids')
    id_list = json.loads(ids)
    ret = Letter.objects.filter(id__in=id_list)
    for letter in ret:
        if letter.user.id == userid:
            letter.delete()
    return JsonResponse({})


def show_letter(request, letterid):
    userid = request.session.get('userid')
    letter_obj = Letter.objects.filter(id=letterid, user_id=userid)
    if letter_obj:
        letter_obj = letter_obj[0]
        letter_list = Letter.objects.all().filter(user_id=userid)
        return render(request, 'letter.html', locals())
    else:
        return redirect('/letter/')


def letter(request):
    if request.method == 'GET':
        userid = request.session.get('userid')
        letter_list = Letter.objects.all().filter(user_id=userid)
        return render(request, 'letter.html', locals())
    else:
        userid = request.session['userid']
        title = request.POST.get("title")
        # subject = request.POST.get("subject")
        comment_content = request.POST.get("comment_content")
        # print(userid,title,subject,comment_content)
        Letter.objects.create(
            title=title,
            # subject=subject,
            content=comment_content,
            user_id=userid
        )

        return redirect('/letter/')


def fanyi(request):
    return render(request, 'fanyi.html')


def mail(request):
    if request.method == 'GET':
        userid = request.session.get('userid')
        sender_list = Sender.objects.filter(user_id=userid)
        return render(request, 'mail.html', locals())


def local_send_mail(email, password, protocol, server, port, send_content):
    subject, message, dest_mail_list, html_message = send_content
    print('*-*-*-**********')
    print(port, type(port))
    print('*-*-*-**********')
    if int(port) == 25:
        settings.EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
        settings.EMAIL_USE_SSL = False
    elif int(port) == 465:
        settings.EMAIL_PORT = 465  # 发件箱的SMTP服务器端口
        settings.EMAIL_USE_SSL = True
    settings.EMAIL_HOST = server
    settings.EMAIL_HOST_USER = email  # 发送邮件的邮箱地址
    settings.EMAIL_HOST_PASSWORD = password  # 发送邮件的邮箱密码(这里使用的是授权码)settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    try:
        ret = send_mail(subject, message, email, dest_mail_list, html_message=html_message, fail_silently=False)
        # ret = False
        return ret
    except Exception as e:
        print(e)
        print(e)
        ret = False
    index = 0
    url_list = [
        'http://47.111.189.77:8081/send_mail_extend/',
        'http://8.212.21.205:8080/send_mail_extend/'
    ]
    while index < len(url_list):
        # url = 'http://47.111.189.77:8081/send_mail_extend/'
        # url = 'http://8.210.131.209:8080/send_mail_extend/'
        url = url_list[index]
        print(url)
        # print(url)
        # print(dest_mail_list)
        print('************')
        params = {
            "subject": subject,
            "message": message,
            "email": email,
            "dest_mail_list": dest_mail_list[0],
            "html_message": html_message,
            "port": port,
            "server": server,
            "password": password,
        }
        response = requests.get(url, params=params)

        print('-*-*-*-*-' * 20)
        # print(response)
        # print(response.content.decode())
        response = response.content.decode()
        if response == '0':
            ret = False
            index += 1
            continue
        else:
            print('yes yes yes')
            ret = True
            break
    return ret


def email_record(request):
    # return HttpResponse("功能维护中!")
    userid = request.session.get('userid')
    pagenum = request.GET.get('pagenum', 1)
    ip = request.META.get("REMOTE_ADDR")
    email_records = EmailRecord.objects.filter(user_id=userid, ip=ip).order_by('-send_time')
    # email_records = EmailRecord.objects.filter(user__username="华能机械").order_by('-send_time')
    print(len(email_records))

    paginator = Paginator(email_records, 200)
    print(paginator.num_pages)
    total_nums = paginator.num_pages
    if int(pagenum) < 1:
        pagenum = 1

    if int(pagenum) > paginator.num_pages:
        pagenum = paginator.num_pages

    print('----------------------------')

    email_records = paginator.page(pagenum)
    return render(request, 'email_record.html', locals())


def delete_record(request):
    userid = request.session.get('userid')
    ids = request.POST.get('recordid')
    id_list = json.loads(ids)
    ret = EmailRecord.objects.filter(id__in=id_list)
    for target in ret:
        if target.user.id == userid:
            target.delete()
    return JsonResponse({})


def test_email(request):
    if request.method == 'POST':
        userid = request.session.get('userid')
        email = request.POST.get('email')
        password = request.POST.get('password')
        protocol = request.POST.get('protocol')
        server = request.POST.get('server')
        port = request.POST.get('port')

        conn = connections['oa_db']
        cursor = conn.cursor()
        if server != "c3.icoremail.net":
            auth_code = request.POST.get('auth_code')

            sql = "select * from ss_authorizemail where code=%s and mail='' "
            cursor.execute(sql, [auth_code])
            ret = cursor.fetchall()
            if ret:
                flag = 1
            else:
                tips = "授权码无效！！！"
                return JsonResponse({
                    'msg': tips
                })
        else:
            flag = 0

        subject = "测试主题"
        message = "测试"
        dest_mail_list = ["790187177@qq.com"]
        html_message = "<p>this is test!!!</p>"
        send_content = (subject, message, dest_mail_list, html_message)

        res = local_send_mail(email, password, protocol, server, port, send_content)
        print(res)
        if res:
            # 发送成功
            ret = {
                'code': 1,
                'msg': '测试成功！'
            }
        else:
            ret = {
                'code': 0,
                'msg': '测试失败，请填写正确的信息！'
            }
        return JsonResponse(ret)


def add_mail(request):
    if request.method == 'POST':
        conn = connections['oa_db']
        cursor = conn.cursor()

        userid = request.session.get('userid')
        email = request.POST.get('email')
        password = request.POST.get('password')
        protocol = request.POST.get('protocol')
        server = request.POST.get('server')
        port = request.POST.get('port')

        if not all([email, password, protocol, server, port]):
            tips = "请填写完整后提交！！！"
            return render(request, 'tips.html', {'tips': tips})

        if server != "c3.icoremail.net":
            auth_code = request.POST.get('auth_code')

            sql = "select * from ss_authorizemail where code=%s and mail='' "
            cursor.execute(sql, [auth_code])
            ret = cursor.fetchall()
            if ret:
                flag = 1
            else:
                tips = "授权码无效！！！"
                return render(request, 'tips.html', {'tips': tips})
        else:
            flag = 0

        subject = "测试主题"
        message = "测试"
        dest_mail_list = ["790187177@qq.com"]
        html_message = "<p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p><p>this is test!!!</p>"
        send_content = (subject, message, dest_mail_list, html_message)

        ret = local_send_mail(email, password, protocol, server, port, send_content)
        print(ret)
        if ret:
            if flag == 1:
                customer = request.session.get('username')
                sql = "update ss_authorizemail set mail=%s,customer=%s where code=%s"
                cursor.execute(sql, [email, customer, auth_code])

            Sender.objects.update_or_create(defaults=
            {
                'user_id': userid,
                "password": password,
                "protocol": protocol,
                "server": server,
                "port": port,
            }, email=email, )
            # 发送成功，添加至数据库
            # Sender.objects.create(user_id=userid,
            #                       email=email,
            #                       password=password,
            #                       protocol=protocol,
            #                       server=server,
            #                       port=port)
            return redirect('/mail/')
        else:
            tips = "填入发件箱信息无法正确发送邮件，请检查信息是否正确！！！"
            return render(request, 'tips.html', {'tips': tips})


def upload_email(request):
    userid = request.session.get('userid')
    file = request.FILES.get("upload_file")
    if not file.name.endswith('.csv'):
        tips = "请下载实例文件，按需修改后上传文件！！！"
        return render(request, 'tips.html', {'tips': tips})

    data = file.read().decode('gbk')
    data_list = data.split('\r\n')[1:]
    error_email = []
    for i in data_list:
        if i:
            try:
                email, password, protocol, port, server = i.split(',')
            except:
                tips = "请按照格式正确填写后提交！！！"
                return render(request, 'tips.html', {'tips': tips})
            print(email, password, protocol, port)

            if server == 'c3.icoremail.net':
                subject = "测试主题"
                message = "测试"
                dest_mail_list = ["790187177@qq.com"]
                html_message = "<p>this is test!!!</p>"
                send_content = (subject, message, dest_mail_list, html_message)

                ret = local_send_mail(email, password, protocol, server, port, send_content)
                print(ret)
                if ret:
                    Sender.objects.update_or_create(defaults=
                    {
                        'user_id': userid,
                        "password": password,
                        "protocol": protocol,
                        "server": server,
                        "port": port,
                    }, email=email, )

                else:
                    error_email.append(email)
            else:
                error_email.append(email)

    if error_email:
        s = ",".join(error_email)
        tips = '以下邮箱未通过测试，若添加非c3.icoremail.net服务器的邮箱（比如163、qq等），请联系客服索要授权码后手动添加！' + s
        return render(request, 'tips.html', {'tips': tips})

    else:
        return redirect('/mail/')


def download_csv(request):
    file_name = request.GET.get('file')
    print(file_name)

    print(os.getcwd())
    file_path = os.path.join(os.getcwd(), 'csv_model', file_name)
    print(file_path)
    # file_path = os.getcwd()
    # file = open(os.getcwd() + '\\csv_model\\mails.csv' + , 'rb')  # Windows下载路径
    # print(os.getcwd() + '\\userfile\\admin\\' + filename)  # Mac测试用下载路径
    file = open(file_path, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(file_name)
    return response


def send_mail_thread(ip, ret, customer_list, letter_list, sender_list, userid):
    for cust_obj in customer_list:
        time.sleep(10)
        keyword = cust_obj.keyword
        try:
            lid = random.choice(letter_list)
            sid = random.choice(sender_list)
            letter_obj = Letter.objects.get(id=lid)
            sender_obj = Sender.objects.get(id=sid)
        except Exception as e:
            print(e)
            tips = '提交数据出错，请选择正确数据提交！！！！'
            ret["msg"] = tips
            ret['code'] = 0
            return JsonResponse(ret)
        # print(letter_obj, sender_obj)

        subject = letter_obj.title
        message = letter_obj.content
        dest_mail_list = [cust_obj.email]
        html_message = letter_obj.content
        send_content = (subject, message, dest_mail_list, html_message)

        # print(send_content)
        #
        ret = local_send_mail(sender_obj.email, sender_obj.password, sender_obj.protocol, sender_obj.server,
                              sender_obj.port, send_content)
        print('********************')
        print(ret)
        print('********************')
        send_status = True if ret else False
        print(cust_obj.email)

        try:
            EmailRecord.objects.create(
                keyword=keyword,
                dest_mail=cust_obj.email,
                # dest_company=cust_obj.company,
                # dest_webiste=cust_obj.website,
                send_status=send_status,
                letter_title=letter_obj.title,
                # letter_content=letter_obj.content,
                send_email=sender_obj.email,

                protocol=sender_obj.protocol,
                port=sender_obj.port,
                server=sender_obj.server,
                user_id=userid,
                ip=ip
            )
        except Exception as e:
            print(e)
    # customer_list.delete()


def send_single_email__ajax(ip, ret, cust_obj, letter_list, sender_list, userid):
    keyword = cust_obj.keyword
    try:
        lid = random.choice(letter_list)
        # print(letter_list)
        # print(lid)
        sid = random.choice(sender_list)
        letter_obj = Letter.objects.get(id=lid)
        sender_obj = Sender.objects.get(id=sid)

    except Exception as e:
        print(e)
        print(e)
        print(e)
        print(e)
        ret["msg"] = '提交数据出错，请选择正确数据提交！！！！'
        ret['code'] = 0
        return ret

    subject = letter_obj.title
    message = letter_obj.content
    dest_mail_list = [cust_obj.email]
    html_message = letter_obj.content
    send_content = (subject, message, dest_mail_list, html_message)

    # print(send_content)
    res = local_send_mail(sender_obj.email, sender_obj.password, sender_obj.protocol, sender_obj.server,
                          sender_obj.port, send_content)

    # print('***************---------------*****')
    # print(res)
    # print('***************---------------*****')

    send_status = True if res else False
    print(cust_obj.email)

    try:
        EmailRecord.objects.create(
            keyword=keyword,
            dest_mail=cust_obj.email,
            # dest_company=cust_obj.company,
            # dest_webiste=cust_obj.website,
            send_status=send_status,
            letter_title=letter_obj.title,
            # letter_content=letter_obj.content,
            send_email=sender_obj.email,

            protocol=sender_obj.protocol,
            port=sender_obj.port,
            server=sender_obj.server,
            user_id=userid,
            ip=ip
        )
        ret['code'] = 1
    except Exception as e:
        print(e)
        print('error2222222222222')
        ret['code'] = 0
    return ret


def send_mail_extend(request):
    subject = request.GET.get('subject')
    message = request.GET.get('message')
    email = request.GET.get('email')
    dest_mail_list = request.GET.get('dest_mail_list')
    html_message = request.GET.get('html_message')
    port = request.GET.get('port')
    server = request.GET.get('server')
    password = request.GET.get('password')
    # print('】】】】呀呀呀呀呀呀晕晕晕晕')
    # print(dest_mail_list,type(dest_mail_list))
    # print('】】】】呀呀呀呀呀呀晕晕晕晕')
    try:
        if int(port) == 25:
            settings.EMAIL_PORT = 25  # 发件箱的SMTP服务器端口
            settings.EMAIL_USE_SSL = False
        elif int(port) == 465:
            settings.EMAIL_PORT = 465  # 发件箱的SMTP服务器端口
            settings.EMAIL_USE_SSL = True
        settings.EMAIL_HOST = server
        settings.EMAIL_HOST_USER = email  # 发送邮件的邮箱地址
        settings.EMAIL_HOST_PASSWORD = password  # 发送邮件的邮箱密码(这里使用的是授权码)settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        ret = send_mail(subject, message, email, [dest_mail_list], html_message=html_message, fail_silently=False)

    except Exception as e:
        print(e)
        ret = 0
    return HttpResponse(str(ret))


def send_mail_ajax(request):
    userid = request.session.get('userid')
    # letter_list = request.POST.getlist('letter_list')
    # letter_list2 = request.POST.getlist('letter_list2')
    # sender_list = request.POST.getlist('sender_list')
    # wait_list = request.POST.getlist('wait_list')

    letter_list = request.POST.get('letter_str', "")
    sender_list = request.POST.get('send_str', "")

    wait_id = request.POST.get('wait_id', '')

    letter_list = letter_list.split(',')
    sender_list = sender_list.split(',')

    # print(letter_list)
    # print(sender_list)

    customer_list = WaitSendCustomer.objects.filter(id=wait_id)
    ret = {
        'wait_id': wait_id,
    }
    if not all([letter_list, sender_list, customer_list]):
        # print('error1111111111111111111')
        tips = '请勾选有效数据后发送邮箱！'
        ret["msg"] = tips
        ret['code'] = 0
        return JsonResponse(ret)
    cust_obj = customer_list.first()
    ip = request.META.get("REMOTE_ADDR")
    # print('ip is %s:'%ip)
    ret = send_single_email__ajax(ip, ret, cust_obj, letter_list, sender_list, userid)
    return JsonResponse(ret)


def send_mail_crm(request):
    # return HttpResponse("功能维护中！请等待！")
    if request.method == 'GET':
        userid = request.session.get('userid')
        kid = request.GET.get('kid', '-1')
        sender_list = Sender.objects.filter(user_id=userid)
        letter_list = Letter.objects.filter(user_id=userid)
        keyword_list = SearchKey.objects.filter(user_id=userid)
        pagenum = request.GET.get('pagenum', '1')

        if kid == '-1':
            waitcust_list = WaitSendCustomer.objects.filter(user_id=userid).order_by('-update_time')
        else:
            keyword = keyword_list.get(id=kid).keyword
            print(keyword)
            waitcust_list = WaitSendCustomer.objects.filter(user_id=userid, keyword=keyword).order_by('-update_time')

        paginator = Paginator(waitcust_list, 200)
        print(paginator.num_pages)
        total_nums = paginator.num_pages
        if int(pagenum) < 1:
            pagenum = 1
        if int(pagenum) > paginator.num_pages:
            pagenum = paginator.num_pages
        print('----------------------------')
        results = paginator.page(pagenum)

        email_li = []
        id_li = []
        for wait in results:
            email = wait.email
            id = wait.id
            if email in email_li:
                pass
            else:
                email_li.append(email)
                id_li.append(id)
        waitcust_list = zip(email_li, id_li)
        return render(request, 'send_mail.html', locals())
    else:
        userid = request.session.get('userid')
        # letter_list = request.POST.getlist('letter_list')
        # letter_list2 = request.POST.getlist('letter_list2')
        # sender_list = request.POST.getlist('sender_list')
        # wait_list = request.POST.getlist('wait_list')

        letter_list = request.POST.get('letter_str', "")
        sender_list = request.POST.get('send_str', "")
        wait_list = request.POST.get('wait_str', "")

        letter_list = letter_list.split(',')
        sender_list = sender_list.split(',')
        wait_list = wait_list.split(',')

        print(letter_list)
        print(sender_list)
        print(wait_list)

        customer_list = WaitSendCustomer.objects.filter(id__in=wait_list)

        ret = {}
        if not all([letter_list, sender_list, wait_list]):
            tips = '请勾选有效数据后发送邮箱！'
            ret["msg"] = tips
            ret['code'] = 0
            return JsonResponse(ret)

        customer_list = WaitSendCustomer.objects.filter(id__in=wait_list)
        print(customer_list)
        ip = request.META.get("REMOTE_ADDR")
        t1 = Thread(target=send_mail_thread, args=(ip, ret, customer_list, letter_list, sender_list, userid))
        t1.start()

        ret["msg"] = "为防止短时间内发送大量邮箱导致邮箱账号被封禁，发送邮箱任务已添加至服务器后台任务队列，按照一定的时间间隔逐条发送。" \
                     "即将跳转至发送记录界面，您可以通过刷新页面查看最新的发送记录！！！"
        ret['code'] = 1
        return JsonResponse(ret)


#
def import_customer(request):
    userid = request.session.get('userid')
    keyid = request.POST.get('keyid')
    print(keyid)
    if keyid == '-1':
        return redirect('/send_target/')

    keyword = SearchKey.objects.get(id=keyid).keyword
    user_obj = User.objects.get(id=userid)
    data_list = user_obj.searchresult_set.all().filter(keyword=keyword).order_by("-id")
    print(len(data_list))
    # data_list = SearchResult.objects.filter(keyword=keyword)

    sr_list = []
    for data in data_list:
        keyword = data.keyword
        company = data.company
        website = data.website
        email = data.email
        print(email)
        sort_id = data.id
        if not email:
            continue
        if ';' in email:
            email_list = email.split(';')
        else:
            email_list = [email]

        for email in email_list:
            w = WaitSendCustomer(keyword=keyword, email=email, company=company, website=website, user_id=userid,
                                 sort_id=data.id)
            sr_list.append(w)
    WaitSendCustomer.objects.bulk_create(sr_list)
    print(len(sr_list))
    return redirect('/send_target/')


def send_target(request):
    if request.method == 'GET':
        kid = request.GET.get('kid', '-1')
        pagenum = request.GET.get('pagenum', 1)
        userid = request.session.get('userid')
        keyword_list = SearchKey.objects.filter(user_id=userid)
        sender_list = Sender.objects.filter(user_id=userid)
        letter_list = Letter.objects.filter(user_id=userid)
        if kid == '-1':
            waitcust_list = WaitSendCustomer.objects.filter(user_id=userid).order_by('-update_time').order_by('sort_id')
        else:
            keyword = keyword_list.get(id=kid).keyword
            print(keyword)
            waitcust_list = WaitSendCustomer.objects.filter(user_id=userid, keyword=keyword).order_by(
                '-update_time').order_by('sort_id')

        paginator = Paginator(waitcust_list, 500)
        print(paginator.num_pages)
        total_nums = paginator.num_pages
        if int(pagenum) < 1:
            pagenum = 1
        if int(pagenum) > paginator.num_pages:
            pagenum = paginator.num_pages
        print('----------------------------')
        waitcust_list = paginator.page(pagenum)

        final_data = []
        email_li = []
        for wait in waitcust_list:
            email = wait.email
            id = wait.id
            keyword = wait.keyword
            company = wait.company
            website = wait.website
            update_time = wait.update_time
            if email in email_li:
                wait.delete()
            else:
                email_li.append(email)
                final_data.append((id, email, keyword, company, website, update_time))
        return render(request, 'send_target.html', locals())


def add_target2(request):
    if request.method == 'POST':
        userid = request.session.get('userid')
        email = request.POST.get('email')
        company = request.POST.get('company')
        website = request.POST.get('website')
        keyword = request.POST.get('keyword')
        ret = {}

        if not all([email, company, website, keyword]):
            tips = '请填写完整有效的数据后添加！！！'
            ret["msg"] = tips
            ret["code"] = 0
            return JsonResponse(ret)

        try:
            WaitSendCustomer.objects.update_or_create(defaults=
            {
                # 'user_id': userid,
                "company": company,
                "website": website,
                "keyword": keyword,
            }, email=email, user_id=userid)
        except Exception as e:
            print(e)
            ret["msg"] = "服务器内部错误（db_save_error！）"
            ret["code"] = 0
            return JsonResponse(ret)
        ret['code'] = 1
        return JsonResponse(ret)


def add_target(request):
    if request.method == 'POST':
        userid = request.session.get('userid')
        email = request.POST.get('email')
        company = request.POST.get('company')
        website = request.POST.get('website')
        keyword = request.POST.get('keyword')
        if not all([email, company, website, keyword]):
            tips = '请填写完整有效的数据后添加！！！'
            return render(request, 'tips.html', {'tips': tips})

        try:
            WaitSendCustomer.objects.update_or_create(defaults=
            {
                # 'user_id': userid,
                "company": company,
                "website": website,
                "keyword": keyword,
            }, email=email, user_id=userid)
        except Exception as e:
            print(e)

        return redirect('/send_target/')


def upload_target(request):
    userid = request.session.get('userid')
    file = request.FILES.get("upload_file")
    try:
        if not file.name.endswith('.csv'):
            tips = '请上传csv文件，您可以下载实例文件，按需修改后上传文件！！！'
            return render(request, 'tips.html', {'tips': tips})
        data = file.read().decode('utf-8')
        data_list = data.split('\n')
        test_set = set()
        sr_list = []
        for i in data_list:
            if i:
                try:
                    keyword, email = i.split('|')
                    # if not keyword:
                    #     keyword = "Empty keywords"
                    if email in test_set:
                        print('该邮箱已存在:',email)
                        continue
                    test_set.add(email)
                    if email:
                        w = WaitSendCustomer(keyword=keyword, email=email, company="File Import", website="File Import",
                                             user_id=userid)
                        sr_list.append(w)
                except Exception as e:
                    print(e)
                    tips = '请按照格式正确填写后提交！！！'
                    return render(request, 'tips.html', {'tips': tips})

        try:
            WaitSendCustomer.objects.bulk_create(sr_list)
        except:
            tips = '请下载实例文件，按照正确的格式填写后上传文件！！'
            return render(request, 'tips.html', {'tips': tips})


    except Exception as e:
        print(e)
        tips = '请下载实例文件，按需修改后上传文件！！'
        return render(request, 'tips.html', {'tips': tips})
    return redirect('/send_target/')


def delete_target(request):
    userid = request.session.get('userid')
    ids = request.POST.get('custid')
    id_list = json.loads(ids)
    print(id_list)
    ret = WaitSendCustomer.objects.filter(id__in=id_list).delete()
    # print(len(ret))
    # for target in ret:
    #     print('**************')
    #     # if target.user.id == userid:
    #     target.delete()
    #     print('delete ok')
    return JsonResponse({})
