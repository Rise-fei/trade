#
# # with open("demo.html",'wb') as f:
# #
# #     f.write(ret.content)
# #
# # import collections
# # l = [1,2,3,1]
# # s = collections.Counter(l)
# # print(s)
# # print(type(s))
# # for k,v in s.items():
# #     print(k,v)
# '''
#
# import requests
#
# url = "http://lumtest.com/myip.json"
# # # url = "https://www.facebook.com/"
# url = "http://www.google.com"
# url ="http://www.google.com/search?q=pizza&lum_json=1"
# # url = "https://www.exportersindia.com/search.php?srch_catg_ty=prod&term=sofa&cont=IN"
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}
#
#
# # proxies = {'http': 'http://lum-customer-c_0ba1644e-zone-residential:Shengshikeji666@zproxy.lum-superproxy.io:22225',
# #             'https': 'http://lum-customer-c_0ba1644e-zone-residential:Shengshikeji666@zproxy.lum-superproxy.io:22225'
# #            }
#
#
# proxies = {'http': 'http://lum-customer-c_0ba1644e-zone-residential-route_err-pass_dyn:Shengshikeji666@zproxy.lum-superproxy.io:22225',
#             'https': 'http://lum-customer-c_0ba1644e-zone-residential-route_err-pass_dyn:Shengshikeji666@zproxy.lum-superproxy.io:22225'}
#
# #
# # proxies = {'http': 'http://lum-customer-c_0ba1644e-zone-zone2:rhiixqunrysr@zproxy.lum-superproxy.io:22225',
# #             'https': 'http://lum-customer-c_0ba1644e-zone-zone2:rhiixqunrysr@zproxy.lum-superproxy.io:22225'}
# # ret = requests.get(url,headers=headers,proxies=proxies)
# # print(ret.content.decode())
# # url = "https://www.youtube.com/"
# # url = "http://lumtest.com/myip.json"
# ret = requests.get(url=url,headers=headers,proxies=proxies)
# print(ret.content.decode())
#
#
# '''
#
#
# '''
# {"ip":"171.248.160.202","country":"VN","asn":{"asnum":7552,"org_name":"Viettel Group"},"geo":{"city":"Ho Chi Minh City","region":"SG","region_name":"Ho Chi Minh","postal_code":"","latitude":10.8142,"longitude":106.6438,"tz":"Asia/Ho_Chi_Minh","lum_city":"hochiminhcity","lum_region":"sg"}}
# {"ip":"146.60.228.233","country":"DE","asn":{"asnum":3209,"org_name":"Vodafone GmbH"},"geo":{"city":"Duisburg","region":"NW","region_name":"North Rhine-Westphalia","postal_code":"47137","latitude":51.4618,"longitude":6.7688,"tz":"Europe/Berlin","lum_city":"duisburg","lum_region":"nw"}}
# {"ip":"181.21.92.226","country":"AR","asn":{"asnum":22927,"org_name":"Telefonica de Argentina"},"geo":{"city":"Loberia","region":"B","region_name":"Buenos Aires","postal_code":"7635","latitude":-38.15,"longitude":-58.7833,"tz":"America/Argentina/Buenos_Aires","lum_city":"loberia","lum_region":"b"}}
# {"ip":"101.165.112.212","country":"AU","asn":{"asnum":1221,"org_name":"Telstra Corporation Ltd"},"geo":{"city":"Brisbane","region":"QLD","region_name":"Queensland","postal_code":"4000","latitude":-27.4732,"longitude":153.0215,"tz":"Australia/Brisbane","lum_city":"brisbane","lum_region":"qld"}}
#
#
# {"ip":"154.13.29.202","country":"US","asn":{"asnum":55799,"org_name":"IPTELECOM ASIA"},"geo":{"city":"Portland","region":"OR","region_name":"Oregon","postal_code":"97253","latitude":45.5248,"longitude":-122.6789,"tz":"America/Los_Angeles","lum_city":"portland","lum_region":"or"}}
#
# '''
# import requests
# # url = "http://lumtest.com/myip.json"
# url = "https://twitter.com/"
#
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}
#
# proxies = {
#     'http': 'http://lum-customer-c_0ba1644e-zone-residential:Shengshikeji666@zproxy.lum-superproxy.io:22225',
#     'https': 'http://lum-customer-c_0ba1644e-zone-residential:Shengshikeji666@zproxy.lum-superproxy.io:22225',
# }
#
# ret = requests.get(url=url,headers=headers,proxies=proxies)
#
# print(ret.content.decode())
#
# '''
# {"ip":"171.248.160.202","country":"VN","asn":{"asnum":7552,"org_name":"Viettel Group"},"geo":{"city":"Ho Chi Minh City","region":"SG","region_name":"Ho Chi Minh","postal_code":"","latitude":10.8142,"longitude":106.6438,"tz":"Asia/Ho_Chi_Minh","lum_city":"hochiminhcity","lum_region":"sg"}}
# {"ip":"146.60.228.233","country":"DE","asn":{"asnum":3209,"org_name":"Vodafone GmbH"},"geo":{"city":"Duisburg","region":"NW","region_name":"North Rhine-Westphalia","postal_code":"47137","latitude":51.4618,"longitude":6.7688,"tz":"Europe/Berlin","lum_city":"duisburg","lum_region":"nw"}}
# {"ip":"181.21.92.226","country":"AR","asn":{"asnum":22927,"org_name":"Telefonica de Argentina"},"geo":{"city":"Loberia","region":"B","region_name":"Buenos Aires","postal_code":"7635","latitude":-38.15,"longitude":-58.7833,"tz":"America/Argentina/Buenos_Aires","lum_city":"loberia","lum_region":"b"}}
# {"ip":"101.165.112.212","country":"AU","asn":{"asnum":1221,"org_name":"Telstra Corporation Ltd"},"geo":{"city":"Brisbane","region":"QLD","region_name":"Queensland","postal_code":"4000","latitude":-27.4732,"longitude":153.0215,"tz":"Australia/Brisbane","lum_city":"brisbane","lum_region":"qld"}}
#
# '''
#

#

def lam(x):
    return x[0]+x[1]

dominoes =[[2,2],[1,2],[1,2],[1,1],[1,2],[1,1],[2,2]]
li = [sorted(i) for i in dominoes]
print(li)
li = sorted(li,key=lambda x:x[0])
li = sorted(li,key=lambda x:x[0]+x[1])
print(li)
count = []
index = 1
prev = []
for i in li:
    cur = i
    if prev == cur:
        index += 1
        prev = cur
    else:
        if index != 1:
            count.append(index)
        index = 1
        prev = cur
if index != 1:
    count.append(index)
print(count)
total = 0
for n in count:
    total += (n-1)*n/2

print(int(total))

# print(li)
#  1 2 3 4 5      4+3+2+1
#  1 2 3 4          3+2+1
#  1 2 3              2+1
#  1 2                  1




# s = hasCN('dlksak233')
#
# print(s)