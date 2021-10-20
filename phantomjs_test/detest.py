from lxml import etree
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,zh-TW;q=0.6",
    "cookie": "CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; CONSENT=YES+US.zh-CN+201905; HSID=ADxkA6jzRB6Pv9F4f; SSID=A6ROAQ3F_zuaK1Qwr; APISID=h4CpiJt_FUn_veK_/A7UK8BVyKyVS7O5ww; SAPISID=2TgO2q6ZyecVAxuJ/A8ww1CxfRa2RSfpqO; __Secure-3PAPISID=2TgO2q6ZyecVAxuJ/A8ww1CxfRa2RSfpqO; ANID=AHWqTUnfkyQzvSzNuYfwrEoHubemaKVuDbb3pPXl9ZvMvk4cdU0lZjX8JQz3B-Pw; SID=7AfkmR-_98Dy9Ua66h8MC5c4m2GrgPCHhzE0NGMHr39ScQF_L5f1FrZ-fsUuiXgitM0ItA.; __Secure-3PSID=7AfkmR-_98Dy9Ua66h8MC5c4m2GrgPCHhzE0NGMHr39ScQF_HBnPE0Oo0gUU4Ki3S52f8Q.; SEARCH_SAMESITE=CgQI_JEB; NID=210=lPaIxFsNdaY28x2K6O_Zedgjj8hbKszMwk_BUdKsK1S0-k43-8uWpyjES6ZelkTdi1RB-BJJm0b4hhZVBmsnxT9L87QtKqJTNXs5cbna8jYYVnwZ8_Bo1na4Ro3fY-h7QJqyskUDvNGOzKOI6DWqga2ip_dS7kUcOwkS6Li6Cn-sgp95NEEgqmqsBuVK5ng3chZUcg_g1kFq_VKkJaGCSqlGuD5CLODSSR29m8_bWY1CKQEiTmvwvkMJq7nCpDe221HUrQZPgCRKe33YgKZYxtArlNKYjxXGwgx-LXgtDiJ2YYUbPOg; GOOGLE_ABUSE_EXEMPTION=ID=79977cac782de7db:TM=1614321853:C=r:IP=67.198.196.100-:S=APGng0uzROmwcWKWPvVFC9ntluRvJMCuCw; 1P_JAR=2021-02-26-07; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjE0MzIzNDAzOTk4MDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDM0MDUyMjM0MgogIGxvbmdpdHVkZV9lNzogLTExODI0MzY4NDkKfQpyYWRpdXM6IDE3MDc1NDIwCnByb3ZlbmFuY2U6IDYK",
    "referer": "https://www.google.com.hk/",
    "sec-ch-ua": '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
}
proxies_google_search = {
    'http': 'http://lum-customer-c_0ba1644e-zone-zone2:rhiixqunrysr@zproxy.lum-superproxy.io:22225',
    'https': 'http://lum-customer-c_0ba1644e-zone-zone2:rhiixqunrysr@zproxy.lum-superproxy.io:22225'
}
proxies_home = {
    'http': 'http://lum-customer-sstrade-zone-residential-country-us:Shengshikeji666@zproxy.lum-superproxy.io:22225',
    'https': 'http://lum-customer-sstrade-zone-residential-country-us:Shengshikeji666@zproxy.lum-superproxy.io:22225'
}
proxies = proxies_home
url = "http://www.google.com/search?q={}".format("sofa")
print(url)
#response = requests.get(url, headers=headers,proxies=proxies_google_search)
response = requests.get(url, headers=headers,proxies=proxies)
with open('aaaaaaaaaaaa.html','wb') as f:
    f.write(response.content)

e = etree.HTML(response.text)
block_list = e.xpath('//div[@class="g"]')
print(len(block_list))
