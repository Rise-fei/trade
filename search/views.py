from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from user import models as user_models
from django.conf import settings
from django.db import connection
from search import models as search_models
import requests
import pymysql
import json
import time
import threading
import random
from django.db import connections
# Create your views here.
import re
from datetime import datetime
from user.models import RequestCount


def test2(request):
    keyword = "fastener"
    num = 1
    id_set = user_models.SearchResult.objects.all().filter(keyword=keyword).values_list(
        'id')
    id_list = [i[0] for i in id_set]
    request.session["id_list"] = id_list
    request.session["keyword"] = keyword
    request.session["len_id_list"] = len(id_list)
    request.session['per_page'] = len(id_list) // 100
    per_page = int(request.session['per_page'])
    start = num * per_page
    end = start + per_page
    id_list = request.session["id_list"]
    print('查询区间 %s ---> %s' % (start, end))

    userid = request.session.get('userid')
    user_obj = user_models.User.objects.get(id=userid)
    print('*************')

    query_list = id_list[start:end]
    print(query_list)
    print(userid)
    data_set = user_models.SearchResult.objects.all().filter(id__in=query_list)
    print('真实数据长度：', len(data_set))
    print(type(data_set))
    print(data_set)
    # data_set2 = user_models.SearchResult.objects.all().filter(keyword=keyword)[0:100]
    # print(data_set2)
    for i in data_set:
        print(i.id,i.keyword)
    tt = threading.Thread(target=add_user_resultdata, args=(user_obj, data_set))
    tt.start()
    return HttpResponse('ok')

def hasCN(string: str):
    """
    判断是否包含汉字(简体中文)
    :param string:
    :return:
    """
    return re.compile(u'[\u4e00-\u9fa5]').search(string)


def issensitive(request):
    keyword = request.POST.get("keyword")
    word_list = user_models.SensitiveWord.objects.all()
    code = 1
    try:
        for word in word_list:
            if keyword.replace(" ", "").upper() == word.word.replace(" ", "").upper():
                print(word.id)
                print(word.word)
                code = 0
                break
    except:
        code = 0
    ret = {
        'code': code,
    }
    return JsonResponse(ret)


'''
def get_socials(request):
    website = request.POST.get("website")
    searchid = request.POST.get("searchid")
    index = 0
    ret = {}
    while index<5:
        try:
            ip_port = random.choice(settings.SERVER_LIST)
            url = "http://%s/get_socials/?website=%s" % (ip_port, website)
            ret = requests.get(url).content.decode()
            ret = json.loads(ret)
            if not ret:
                index += 1
                continue
            else:
                break
        except Exception as e:
            print(e)
            index += 1
            continue

    if ret:
        user = user_models.SearchResult.objects.get(id=searchid)
        try:
            if ret.get('email'):

                if '.gov' in ret.get('email') or '.edu' in ret.get('email'):
                    pass
                else:
                    if user.email:
                        s = user.email + ";" + ret.get('email')
                        l = list(set(s.split(";")))
                        if "" in l:
                            l.remove("")
                        user.email = ";".join(l)[1:]
                    else:
                        user.email = ret.get('email')

            if ret.get('phone'):
                if user.phone:
                    s = user.phone + ";" + ret.get('phone')
                    l = list(set(s.split(";")))
                    if "" in l:
                        l.remove("")
                    user.phone = ";".join(l)[1:]
                else:
                    user.phone = ret.get('phone')

            if ret.get('facebook'):
                if user.facebook:
                    s = user.facebook + ";" + ret.get('facebook')
                    l = list(set(s.split(";")))
                    if "" in l:
                        l.remove("")
                    user.facebook = ";".join(l)[1:]
                else:
                    user.facebook = ret.get('facebook')

            if ret.get('twitter'):
                if user.twitter:
                    s = user.twitter + ";" + ret.get('twitter')
                    l = list(set(s.split(";")))
                    if "" in l:
                        l.remove("")
                    user.twitter = ";".join(l)[1:]
                else:
                    user.twitter = ret.get('twitter')

            user.save()
        except Exception as e:
            print(e)

        ret = {
            'email': user.email,
            'phone': user.phone,
            'facebook': user.facebook,
            'twitter': user.twitter,
        }

        res = {
            'data':ret,
            'searchid':searchid,
        }
    else:
        res = {
            'data': None,
            'searchid': searchid,
        }
    return JsonResponse(res)
'''

def get_socials(request):
    save_db(1)
    save_db2(request.session['username'], 1)
    website = request.POST.get("website")
    searchid = request.POST.get("searchid")
    ret = {}

    user = user_models.SearchResult.objects.get(id=searchid)
    if user.email:
        ret = {
            'email': user.email,
            'phone': user.phone,
            'facebook': user.facebook,
            'twitter': user.twitter,
        }
        res = {
            'msg': '数据库中该数据已经有邮箱，查询成功！',
            'data': ret,
            'searchid': searchid,
        }
        return JsonResponse(res)

    try:
        ip_port = random.choice(settings.SERVER_LIST)
        url = "http://%s/get_socials/?website=%s" % (ip_port, website)
        ret = requests.get(url).content.decode()
        ret = json.loads(ret)
        if not ret:
            res = {
                'msg': '数据未成功爬取，爬虫服务器返回数据为空，服务器未响应到邮箱数据！',
                'data': None,
                'searchid': searchid,
            }
            return JsonResponse(res)
    except Exception as e:
        print(e)
        res = {
            'msg': '服务器链接异常，该网址可能已失效！',
            'data': None,
            'searchid': searchid,
        }
        return JsonResponse(res)

    try:
        if ret.get('email'):
            user.email = ret.get('email')
        if ret.get('phone'):
            if user.phone:
                s = user.phone + ";" + ret.get('phone')
                l = list(set(s.split(";")))
                if "" in l:
                    l.remove("")
                user.phone = ";".join(l)[1:]
            else:
                user.phone = ret.get('phone')

        if ret.get('facebook'):
            # if user.facebook:
            #     s = user.facebook + ";" + ret.get('facebook')
            #     l = list(set(s.split(";")))
            #     if "" in l:
            #         l.remove("")
            #     user.facebook = ";".join(l)[1:]
            # else:
            user.facebook = ret.get('facebook')

        if ret.get('twitter'):
            # if user.twitter:
            #     s = user.twitter + ";" + ret.get('twitter')
            #     l = list(set(s.split(";")))
            #     if "" in l:
            #         l.remove("")
            #     user.twitter = ";".join(l)[1:]
            # else:
            user.twitter = ret.get('twitter')

    except Exception as e:
        print(e)
    user.save()
    ret = {
        'email': user.email,
        'phone': user.phone,
        'facebook': user.facebook,
        'twitter': user.twitter,
    }

    res = {
        'msg': '数据爬取成功并返回！',
        'data': ret,
        'searchid': searchid,
    }

    return JsonResponse(res)


'''
def get_email(request):

    website = request.POST.get("website")
    searchid = request.POST.get("searchid")

    index = 0
    email = None
    while index < 5:
        try:
            ip_port = random.choice(settings.SERVER_LIST)
            url = "http://%s/get_mail/?website=%s" % (ip_port,website)
            print(url)
            ret = requests.get(url).content.decode()
            print(ret)
            ret = json.loads(ret)
            email = ret["mail"]
            if '.gov' in email or '.edu' in email:
                res = {
                    'email': "",
                    'searchid': searchid,
                }
                return JsonResponse(res)

            if email:
                break
            else:
                index += 1
                continue
        except Exception as e:
            print(e)
            index += 1
            continue

    if email:
        user = user_models.SearchResult.objects.get(id=searchid)
        if user.email:
            s = user.email + ";" + email
            l = list(set(s.split(";")))
            if "" in l:
                l.remove("")
            user.email = ";".join(l)[1:]
        else:
            user.email = email
        user.save()
        res = {
            'email':email,
            'searchid':searchid,
        }
    else:
        res = {
            'email': "",
            'searchid': searchid,
        }
    return JsonResponse(res)
'''


def get_email(request):
    save_db(1)
    save_db2(request.session['username'], 1)
    website = request.POST.get("website")
    searchid = request.POST.get("searchid")

    user = user_models.SearchResult.objects.get(id=searchid)
    if user.email:
        res = {
            'msg': '数据库中已经存在邮箱，查询并返回！',
            'email': user.email,
            'searchid': searchid,
        }
        return JsonResponse(res)

    server_list = settings.SERVER_LIST
    random.shuffle(server_list)

    for server in server_list:
        try:
            # ip_port = random.choice(settings.SERVER_LIST)
            ip_port = server
            url = "http://%s/get_mail/?website=%s" % (ip_port, website)
            print(url)
            ret = requests.get(url).content.decode()
            print(ret)
            ret = json.loads(ret)
            email = ret.get('mail')
            if email:
                if '.gov' in email or '.edu' in email:
                    res = {
                        'msg': '该邮箱包含教育或政府信息',
                        'email': "",
                        'searchid': searchid,
                    }
                    return JsonResponse(res)
                else:
                    break
        except Exception as e:
            print(e)
            continue
    else:
        res = {
            'msg': '爬取服务器出现异常！',
            'email': "",
            'searchid': searchid,
        }
        return JsonResponse(res)

    user.email = email
    user.save()
    res = {
        'msg': '爬取邮箱成功！',
        'email': email,
        'searchid': searchid,

    }
    return JsonResponse(res)

def test(request):
    save_db(11)
    return HttpResponse(1)

def save_db(count=0):
    try:
        conn = connections['beijingdb']
        print(conn)
        cursor = conn.cursor()
        print(cursor)

        time_str = time.strftime("%Y-%m-%d")
        print(time_str)
        sql = "select * from web_record WHERE DATE_FORMAT(date, '%%Y-%%m-%%d')=%s;"
        cursor.execute(sql, [time_str])
        result = cursor.fetchall()
        if not result:
            sql = "insert into web_record values(0,%s,0)"
            cursor.execute(sql, [time_str])
        print(result)

        add_sql = "UPDATE web_record set count=count+%s where DATE_FORMAT(date, '%%Y-%%m-%%d')=%s;"
        cursor.execute(add_sql, [count, time_str])
        cursor.close()
        conn.close()
    except Exception as e:
        print('保存至web_record表中出现异常')
        print(e)


def save_db2(cname,count):
    try:
        cust_name = cname
        month = datetime.now().month
        year = datetime.now().year
        rc = RequestCount.objects.filter(month=month, year=year, customer=cust_name)
        if rc:
            rc = rc[0]
        else:
            rc = RequestCount.objects.create(count=0, month=month, year=year, customer=cust_name)
        rc.count = rc.count + count
        rc.save()
    except Exception as e:
        print(e)
        print('save_db2 error。。。')

def results(request):
    userid = request.session.get('userid')
    keywords = user_models.SearchKey.objects.filter(user_id=userid)
    key = request.GET.get("keyword")
    dataset = request.GET.get("dataset")
    pagenum = request.GET.get('pagenum', '1')
    if key:
        try:
            key = user_models.SearchKey.objects.get(id=key).keyword
            user_obj = user_models.User.objects.get(id=userid)
            results = user_obj.searchresult_set.all()

            if dataset == '1':
                results = results.filter(query_flag=1)
            elif dataset == '2':
                results = results.filter(query_flag=2)
            else:
                pass
            results = results.filter(keyword=key).order_by('-id')
            print('----------------------------')
            paginator = Paginator(results, 200)
            print(paginator.num_pages)
            total_nums = paginator.num_pages
            if int(pagenum) < 1:
                pagenum = 1
            if int(pagenum) > paginator.num_pages:
                pagenum = paginator.num_pages
            print('----------------------------')
            results = paginator.page(pagenum)

        except Exception as e:
            print(e)
    return render(request, 'search/search_results.html', locals())


def add_user_resultdata(user_obj,data_set):
    print(len(data_set),type(data_set))
    user_obj.searchresult_set.add(*data_set)

def engine(request):
    userid = request.session.get('userid')
    if request.method == 'GET':
        # li = [i*5 for i in range(1,21)]
        sen_words = user_models.SensitiveWord.objects.all()
        return render(request, 'search/search_engine.html', locals())
    elif request.method == 'POST':
        keyword = request.POST.get('keyword', "")
        # keyword = keyword.replace(" ",'+')
        num = request.POST.get('num')
        engine = request.POST.get('engine')

        user_models.SearchKey.objects.update_or_create(defaults=
        {
        }, keyword=keyword, user_id=userid)

        hour = time.localtime().tm_hour

        num = int(num)


        if hour >= 22 or hour < 8:
        # if hour >= 8 or hour < 1                                                              8:
            print('系统维护时间段，搜索数据库！')
            print('当前页码：%s' % num)
            print('系统维护时间段，搜索数据库！')
            if num == 0:
                id_set = user_models.SearchResult.objects.all().filter(keyword=keyword).values_list(
                    'id')
                id_list = [i[0] for i in id_set]
                request.session["id_list"] = id_list
                request.session["keyword"] = keyword
                request.session["len_id_list"] = len(id_list)
                request.session['per_page'] = len(id_list) // 100

                data = {
                    'code': 0,
                    "data": []
                }
                return JsonResponse(data)

            if request.session.get("keyword") != keyword:
                id_set = user_models.SearchResult.objects.all().filter(keyword=keyword).values_list(
                    'id')
                id_list = [i[0] for i in id_set]
                request.session["id_list"] = id_list
                request.session["keyword"] = keyword
                request.session["len_id_list"] = len(id_list)
                request.session['per_page'] = len(id_list) // 100 # 32456 ---> 324

            per_page = int(request.session['per_page'])
            start = num * per_page
            end = start + per_page
            id_list = request.session["id_list"]
            print('查询区间 %s ---> %s' % (start,end))
            query_list = id_list[start:end]
            data_set = user_models.SearchResult.objects.all().filter(id__in=query_list)
            print('真实数据长度：',len(data_set))
            print(type(data_set))
            # try:
            #     # data_set = user_models.SearchResult.objects.all().filter(keyword__icontains=keyword)[start:end]
            #     pass
            # except:
            #     print('抽取软件是数据库中的数据', num)
            #     conn = connections["newtrade"]
            #     cursor = conn.cursor()
            #     sql = "select title,website,description,mail from data_table where kw_id in (select id from keyword_table where keyword like %s)"
            #     cursor.execute(sql, ['%' + keyword + '%'])
            #     ret = cursor.fetchall()
            #     print(len(ret))
            #     data_list = {
            #         "data": []
            #     }
            #     #
            #     if not request.session.get('per_page'):
            #         ret_len = len(ret)     # 60 - 100           0 - 1000
            #         per_page = ret_len // (100 - num + 1)
            #         request.session["per_page"] = per_page
            #         request.session["start_num"] = num
            #         start_num = num
            #     else:
            #         per_page = request.session.get("per_page",100)
            #         start_num = request.session.get("start_num",0)
            #
            #     s_start = (num - start_num) * per_page
            #     s_end = s_start + per_page
            #
            #     try:
            #         for i in ret[s_start:s_end]:
            #             di = {
            #                 'title': i[0],
            #                 'website': i[1],
            #                 'description': i[2],
            #                 'mail': i[3],
            #             }
            #             s = ""
            #             try:
            #                 s = i[0] + i[1] + i[2] + i[3]
            #             except:
            #                 pass
            #
            #             if 'china' in s.lower() or 'alibaba' in s.lower():
            #                 continue
            #             else:
            #                 data_list["data"].append(di)
            #     except:
            #         pass
            #
            #
            #     cursor.close()
            #     conn.close()
            #
            #     userid = request.session.get('userid')
            #     t = threading.Thread(target=save_databases, args=(keyword, data_list, userid))
            #     t.start()
            #
            #     data = {
            #         'code': 1,
            #         "data": data_list
            #     }
            #     return JsonResponse(data)


            user_obj = user_models.User.objects.get(id=userid)
            print(user_obj.username)
            print('*************')
            # user_obj.searchresult_set.add(*data_set)
            tt = threading.Thread(target=add_user_resultdata,args=(user_obj,data_set))
            tt.start()
            print('添加成功')
            print('*************')
            print(len(data_set))
            li = []
            for data in data_set:
                di = {}
                di["website"] = data.website
                di["title"] = data.company
                di["description"] = data.description
                di["mail"] = data.email
                s = ""
                try:
                    s = data.website + data.company + data.description + data.email
                except:
                    pass

                if 'china' in s.lower() or 'alibaba' in s.lower():
                    continue
                else:
                    li.append(di)
                # print(di)

            print("遍历完毕")
            data_list = {
                'data': li
            }
            data = {
                'code': 1,
                "data": data_list
            }
            return JsonResponse(data)
    
        else:
            # data = {
            #     'code': 0,
            #     "data": []
            # }
            # return JsonResponse(data)
            save_db(1)
            save_db2(request.session['username'],1)

            # 1.直接从原爬虫数据库中查询数据
            if int(num) == -1:


                # data_set = user_models.SearchResult.objects.all().filter(keyword__icontains=keyword)
                data_set = user_models.SearchResult.objects.all().filter(keyword__startswith=keyword)
                user_obj = user_models.User.objects.get(id=userid)
                print('*************')
    
                tt = threading.Thread(target=add_user_resultdata,args=(user_obj,data_set))
                tt.start()
                # user_obj.searchresult_set.add(*data_set)
                print('添加成功')
                print('*************')
                print(len(data_set))
                li = []
                for data in data_set:
                    di = {}
                    di["website"] = data.website
                    di["title"] = data.company
                    di["description"] = data.description
                    di["mail"] = data.email
                    s = ""
                    try:
                        s = data.website + data.company + data.description + data.email
                    except:
                        pass
    
                    if 'china' in s.upper() or 'alibaba' in s.upper():
                        continue
                    else:
                        li.append(di)
                    print(di)
    
                print("遍历完毕")
                data_list = {
                    'data': li
                }
                data = {
                    'code': 1,
                    "data": data_list
                }


                # data = {
                #     'code': 0,
                #     "data": []
                # }
                return JsonResponse(data)

                '''
    
                host = '47.98.164.255'
                user = 'root'
                password = 'Shengshikeji.1'
                database = 'new_tradeinfo'
                port = 3306
                conn = pymysql.Connect(host, user, password, database, port)
                print(conn)
                cur = conn.cursor()
                sql = "select website,title,description,mail from data_table where kw_id IN(select id from keyword_table where keyword like '%{}%')".format(keyword)
                print(sql)
                cur.execute(sql)
                ret = cur.fetchall()
                print(len(ret))
                li = []
                for i in ret:
                    di = {}
                    di["website"] = i[0]
                    di["title"] = i[1]
                    di["description"] = i[2]
                    di["mail"] = i[3]
                    li.append(di)
                    print(di)
                data_list = {
                    'data':li
                }
    
                '''
            # 2.请求爬虫服务器，获得数据
            else:
                flag = 0
                index = 0
                while index < 4:
                    try:
                        ip_port = random.choice(settings.SERVER_LIST)
                        url = "http://%s/get_web_new/?kw=%s&num=%s&engine=%s" % (ip_port, keyword, num, engine)
                        ret = requests.get(url)
                        result = ret.content.decode()
                        print(url)
                        print(num)
                        if result == 'no data' or result == 'engine error':
                            index += 1
                            continue
                        else:
                            flag = 1
                            data_list = json.loads(result)
                            break
                    except Exception as e:
                        # print(e)
                        index += 1
                        continue
                if not flag:
                    data = {
                        'code': 0,
                    }
                    return JsonResponse(data)

        # 将结果2   保存或更新至数据库
        t = threading.Thread(target=save_databases, args=(keyword, data_list, userid))
        t.start()

        data = {
            'code': 1,
            "data": data_list
        }
        return JsonResponse(data)
    else:
        return HttpResponse('error')


def save_databases(keyword, data_list, userid):
    user_obj = user_models.User.objects.get(id=userid)
    print(user_obj)

    cursor = connection.cursor()

    for search_data in data_list["data"]:
        company = search_data.get("title", "")
        website = search_data.get("website", "")
        description = search_data.get("description", "")
        email = search_data.get("mail", "")
        if not company:
            company = ""
        if not website:
            website = ""
        if not description:
            description = ""
        if not email:
            email = ""
        try:
            if not hasCN(company + website + description + email):
                cursor.execute("select * from search_result where company=%s and keyword=%s", [company, keyword])
                ret = cursor.fetchall()
                if ret:
                    print('查找成功！')
                    ret = ret[0]
                    # print(ret)
                    # 从数据库中查询，如果有直接返回！
                    id = ret[0]
                    # keyword = ret[1]
                    # company = ret[2]
                    # website = ret[3]
                    # description = ret[4]
                    # email = ret[5]
                    # addr = ret[6]
                    # phone = ret[7]
                    # website = "ceshi.com"
                    # description = "ceshi.1233"
                    cursor.execute("update search_result set website=%s,description=%s,email=%s where id=%s",
                                   [website, description, email, id])
                    ret = cursor.fetchall()
                    # print(ret)
                    try:
                        cursor.execute("INSERT into search_result_user(searchresult_id,user_id) VALUES(%s,%s)",
                                       [id, userid])
                        ret = cursor.fetchall()
                        print(ret)
                        print('添加至user关系映射表')
                    except Exception as e:
                        print(e)
                        print('已经存在，不必添加')

                else:
                    cursor.execute(
                        "INSERT into search_result(keyword,company,website,description,email,addr,phone,facebook,twitter,query_flag)	VALUES(%s,%s,%s,%s,%s,'','','','',1)",
                        [keyword, company, website, description, email])
                    ret = cursor.fetchall()
                    # print(ret)

                    cursor.execute("SELECT @@IDENTITY")
                    id = cursor.fetchall()
                    print(id[0][0])
                    id = id[0][0]

                    print('%s：添加至数据库' % company)
                    #cursor.execute("select * from search_result where company=%s and keyword=%s", [company, keyword])
                    #ret = cursor.fetchall()
                    #id = ret[0][0]
                    cursor.execute("INSERT into search_result_user(searchresult_id,user_id) VALUES(%s,%s)",
                                   [id, userid])
                    ret = cursor.fetchall()
                    print(ret)
                    print('添加至user关系映射表')

                # print("没有中文 添加！！")
                '''
                try:
                    sr = user_models.SearchResult.objects.update_or_create(defaults=
                    {
                        "keyword": keyword,
                        "website": website,
                        "description": description,
                        # "email": email,
                    }, company=company, )
                    user_obj.searchresult_set.add(sr[0].id)
                    print(sr[0].id)
                    print('*********************')
                except Exception as e:
                    print(e)
                '''
            else:
                print("有中文，不加！")
        except Exception as e:
            print('-*-*-*-*-*-*')
            print(company)
            print(website)
            print(description)
            print(email)
            print(e)

    cursor.close()


def get_yellow_page_nums(request):
    save_db(1)
    save_db2(request.session['username'], 1)
    keyword = request.GET.get("keyword")
    cont = request.GET.get("cont", "")
    index = 0
    while index < 10:
        try:
            ip_port = random.choice(settings.SERVER_LIST)
            url = "http://{}/yellow_page_nums/?keyword={}&cont={}".format(ip_port, keyword, cont)
            print(url)
            ret = requests.get(url=url)
            total = ret.text
            p = json.loads(total)
            print("查询的总数量：", p)
            ret = {
                "code":1,
                "data":p
            }
            return JsonResponse(ret)
        except:
            index += 1
            continue
    ret = {
        'code':0,
    }
    return JsonResponse(ret)

# 暂时不用，用新的 get_yellow_page_nums
def get_export_india_totalnums(request):
    save_db(1)
    save_db2(request.session['username'], 1)
    keyword = request.GET.get("keyword")
    cont = request.GET.get("cont", "")
    ip_port = random.choice(settings.SERVER_LIST)
    url = "http://{}}/exportindia_get_total/?keyword={}&cont={}".format(ip_port, keyword, cont)
    print(url)
    ret = requests.get(url=url)
    # with open('test.html','wb')as f:
    #     f.write(ret.content)
    print(ret.text)
    # total = ret.content.decode()
    total = ret.text
    p = json.loads(total)
    print(p, type(p))
    print("总数量：", total)
    print("总数量：", p)
    # ret = {
    #     "total":total
    # }
    return JsonResponse(p)


def yellow(request):
    if request.method == 'GET':
        sen_words = user_models.SensitiveWord.objects.all()
        userid = request.session.get('userid')
        username = request.session.get('username')
        return render(request, 'search/search_yellow.html', locals())
    else:


        username = request.POST.get("username")
        userid = request.POST.get("userid")
        keyword = request.POST.get("keyword")
        pageno = request.POST.get("num")
        cont = request.POST.get("cont", "")
        method = request.POST.get("method", "")
        save_db(1)
        save_db2(username, 1)
        ret = {}
        index = 0
        while index < 4:
            try:
                ip_port = random.choice(settings.SERVER_LIST)
                if method == "in":
                    url = "http://{}/exportindia/?keyword={}&pageno={}&cont={}".format(ip_port, keyword, pageno, cont)

                elif method == 'ph':
                    url = "http://{}/yellowpages_ph/?keyword={}&pageno={}".format(ip_port, keyword, pageno)
                elif method == 'eu':
                    url = "http://{}/europages/?keyword={}&pageno={}".format(ip_port, keyword, pageno)
                else:
                    return JsonResponse({})
                ret = requests.get(url,timeout=15)
                s = ret.content.decode()
                ret = json.loads(s)
                if ret:
                    break
                else:
                    index += 1
                    continue
            except Exception as e:
                print(e)
                index += 1
                continue

        try:
            userid = request.session.get('userid')
            user_models.SearchKey.objects.update_or_create(defaults=
            {
            }, keyword=keyword, user_id=userid)
        except Exception as e:
            print(e)

        t1 = threading.Thread(target=save_database, args=(ret, keyword, userid))
        t1.start()

        return JsonResponse(ret)


def save_database(ret, keyword, userid):
    user_obj = user_models.User.objects.get(id=userid)
    print(user_obj)

    for search_data in ret["data"]:
        company = search_data.get("company", "")
        website = search_data.get("website", "")
        addr = search_data.get("address", "")
        phone = search_data.get("phone", "")
        email = search_data.get("email", "")
        if not hasCN(company + website + addr + phone + email):
            try:
                sr = user_models.SearchResult.objects.update_or_create(defaults=
                {
                    'website': website,
                    "addr": addr,
                    "phone": phone,
                    "email": email,
                    "query_flag": '2',
                }, keyword=keyword, company=company, )

                user_obj.searchresult_set.add(sr[0].id)
            except Exception as e:
                print(e)


