# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# browser = webdriver.Chrome()
# # cookie = [{'domain': '.linkedin.com', 'expiry': 1613723164, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=VB79:s=V:r=V:g=2705:u=3:i=1613719380:t=1613723164:v=1:sig=AQF-gI1mKOTYOBRtgDetYCTwawLErTrU"'}, {'domain': '.linkedin.com', 'expiry': 1629271357, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-637568504%7CMCIDTS%7C18678%7CMCMID%7C45117555243484929122668973899777187689%7CMCAAMLH-1614324157%7C11%7CMCAAMB-1614324157%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1613726557s%7CNONE%7CMCCIDH%7C1636281504%7CvVersion%7C5.1.1'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.linkedin.com', 'expiry': 1616311356, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQHG44T8b1h71AAAAXe5K0OJg-Jx7CdyrByORswn76ORYbZjbVDKiCy65PCgg73KDRAzJ7S-CwCEoHpbeiM58O31txEamt-T'}, {'domain': '.linkedin.com', 'expiry': 1621495380, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '414fa8be-cdb1-4818-8fbf-af47cb69c163'}, {'domain': '.www.linkedin.com', 'httpOnly': False, 'name': 'spectroscopyId', 'path': '/', 'secure': False, 'value': '8c64fd10-1546-4dd0-b4b7-658bef696bc9'}, {'domain': '.www.linkedin.com', 'expiry': 1614928978, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'secure': False, 'value': 'Asia/Shanghai'}, {'domain': '.linkedin.com', 'expiry': 1613719412, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.www.linkedin.com', 'expiry': 1645255352, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDATNUtQMD5QmgAAABd7krNYUAAAF33Te5hVYAD_aH_IipIwVwrGxRTUX1HRLUTqdpfUg7A-PmgFFnrbOadYgrC7gQxjHNzu6rwmD9RIrNBcA4J3KkR4HzBvkCH_FOYaIjPL0XHi5zA7HBxjUWJfjf'}, {'domain': '.linkedin.com', 'expiry': 1616311356, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQHG44T8b1h71AAAAXe5K0OJg-Jx7CdyrByORswn76ORYbZjbVDKiCy65PCgg73KDRAzJ7S-CwCEoHpbeiM58O31txEamt-T'}, {'domain': '.linkedin.com', 'expiry': 1613805752, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.15912504.1613719353'}, {'domain': '.linkedin.com', 'expiry': 1676833203, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&3da390d6-097f-4d11-8d6e-d65f2f0ee20a"'}, {'domain': '.linkedin.com', 'expiry': 1676791352, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.115096357.1613719353'}, {'domain': '.linkedin.com', 'expiry': 1616311380, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'secure': False, 'value': '44911691072987667792721641620434906274'}, {'domain': '.www.linkedin.com', 'expiry': 1621495352, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:7036283530349470880"'}, {'domain': '.linkedin.com', 'expiry': 1621495352, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.www.linkedin.com', 'expiry': 1676833203, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&20210219072231651f01e6-4bbc-4fea-82e7-5ae4b0c42ca3AQEbwza-Zbztx9fwxvinbI1Jbt-gD9rW"'}, {'domain': '.www.linkedin.com', 'expiry': 1614324153, 'httpOnly': False, 'name': 'li_cc', 'path': '/', 'secure': False, 'value': 'AQFBDOqym7QztQAAAXe5KzbhMRjfiTwZVF7JVN5sEIhs5V_jxMtFY4wG9FZTogFAKNi6rrj-ETlU'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=zh-cn'}, {'domain': '.linkedin.com', 'expiry': 1616311380, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQKxjCHazFBXSwAAAXe5K5_T_cqFpiqnJQNghrEEfKhbA2seKmIZoTYm10m11M4CWBmAz_arZgs0E0oTHMrQfROtEzt9dnt1ydfnonYF-56Rz3k57HJg_tJQDJJV7gdOktu1YMtPiLWd01W7Hx5YA4LmSHEajStAYDU3O-1uY0xiv6KAKb7yjJ41vadksppvFOllFZf0fjEWn5UqjJ0NnR51Aq24nSv6Rju0SijhLKSlvNeH4T5QX3jp-WDNxzlt3bnsKUw11iJFqLCnNYiShFcgeoOyh6UDG77yqfY'}, {'domain': '.linkedin.com', 'expiry': 1616311355, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQKvx3_D6RhNbwAAAXe5K0G0oK103DASJv10HjU8oCx0CMtBuvqaBVJiaz1ZXLnj6AQt4MZBfU2JCp6TOZzfyA'}, {'domain': '.www.linkedin.com', 'expiry': 1645255352, 'httpOnly': True, 'name': 'li_rm', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQGZ3GNA3E105AAAAXe5KzDXW0LjL1OelGcLIF0x0XWPIZnm238VynyzDPh2ZC0t3DOIGloCSPrkP71riTl3lsF87YX7KlJyXeqKODciKWqzT4AthupzAw7Q'}]
# # browser.add_cookie(cookie)
#
# #
# browser.get('https://www.linkedin.com/login/')
#
# browser.find_element_by_id('username').send_keys("18669319099")
# browser.find_element_by_id('password').send_keys("liu8581393")
# browser.find_element_by_class_name('login__form_action_container').click()
#
#
# # browser.get('https://www.linkedin.com/feed/')
# print('登录成功')
# cookies = browser.get_cookies()
# print(cookies)
# print(type(cookies))
#
# cookies = [{'domain': '.linkedin.com', 'expiry': 1629362468, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '-637568504%7CMCIDTS%7C18679%7CMCMID%7C66419462578614910562316486471867481845%7CMCAAMLH-1614415268%7C11%7CMCAAMB-1614415268%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1613817668s%7CNONE%7CMCCIDH%7C1636281504%7CvVersion%7C5.1.1'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.linkedin.com', 'expiry': 1613813191, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=TB79:s=T:r=T:g=2577:u=5:i=1613810466:t=1613813190:v=1:sig=AQEkAiyrv2Q0WKR8u572sijvXhorRFsv"'}, {'domain': '.linkedin.com', 'expiry': 1616402466, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQF-sd0ss9wu8wAAAXe-mXyji2MjzqnZ7iXbdwjr8gFjlKd060-anNerd-pHADWR-yk0cxVd0TVZ4fOj6dBZWKsI-ILTojX1'}, {'domain': '.linkedin.com', 'expiry': 1621586466, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '3b865be7-96cc-4afe-8c05-e23f38d42d79'}, {'domain': '.www.linkedin.com', 'httpOnly': False, 'name': 'spectroscopyId', 'path': '/', 'secure': False, 'value': 'f09ef093-16de-40a7-82d2-bde8d6036308'}, {'domain': '.www.linkedin.com', 'expiry': 1615020064, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'secure': False, 'value': 'Asia/Shanghai'}, {'domain': '.linkedin.com', 'expiry': 1613810523, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.www.linkedin.com', 'expiry': 1645346462, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDATNUtQMAl1NIAAABd76ZbaIAAAF34qXxolYAMIGcmb1k6D_96o7V_oyc-8d7YAnPJj0pbHg4fgcy8WnEFxW8hFZ4mgPIxUSzf5Y_zoZeuiKEqhFXJ4nZhlRc66R1qZUm1hvQkbzfQsKy-qiQ4VtF'}, {'domain': '.linkedin.com', 'expiry': 1616402466, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQF-sd0ss9wu8wAAAXe-mXyji2MjzqnZ7iXbdwjr8gFjlKd060-anNerd-pHADWR-yk0cxVd0TVZ4fOj6dBZWKsI-ILTojX1'}, {'domain': '.linkedin.com', 'expiry': 1613896863, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.348004680.1613810463'}, {'domain': '.linkedin.com', 'expiry': 1676924313, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&9d74eaf9-4dff-47a3-881d-e9b878c88941"'}, {'domain': '.linkedin.com', 'expiry': 1676882463, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2047183594.1613810463'}, {'domain': '.linkedin.com', 'expiry': 1616402468, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'secure': False, 'value': '66934065828139690832371988602215877950'}, {'domain': '.www.linkedin.com', 'expiry': 1621586462, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:1235874207640191070"'}, {'domain': '.linkedin.com', 'expiry': 1621586462, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.www.linkedin.com', 'expiry': 1676924313, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&2021022008410126e775f3-5d1d-4f2b-8b6e-c943bd27605eAQH-z0Vepkmx3WM0F90ujnnecP8SpUZR"'}, {'domain': '.www.linkedin.com', 'expiry': 1614415263, 'httpOnly': False, 'name': 'li_cc', 'path': '/', 'secure': False, 'value': 'AQGofMxjDcOvhQAAAXe-mXELN3iKQL1Ww9ZCRG2LK6O0gia8fyo-hvsjyZKuRk9dyIUYj4W9Bn_x'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=zh-cn'}, {'domain': '.linkedin.com', 'expiry': 1616402466, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQJMqiCq8tFxiAAAAXe-mXuLBS319kNsMZQfMJmF0m4T5pnSsUv0dZnQ9At3AKb60zyzrMOrAKa4mG1WYG4jOQ'}, {'domain': '.linkedin.com', 'expiry': 1616402466, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQKaZYO9W6NTcgAAAXe-mXuK5qSzusVpenqStzFClFgfxHxuZG0C19scapGLwTdLEk53TALrWn9eZdew4RlGdEZR7X6f3v_5FEqceygExNi532Pj2GJS6FtHRaubsVR9hfPbajVFTH9ETCuS_qTIeCnT9LGSeIwIoYRdPiPtoW5YCX38-7lscVpgEhNuXO7JHZvzR3azNLzSzgpNsHchTE-oiaGB3uSiuZUQFZwTLBEQpV-MLcU8WXROMAg8O67TFacZERw3wn47Frd1CoFP80dHKao84akT_ryJlQ8'}, {'domain': '.www.linkedin.com', 'expiry': 1645346462, 'httpOnly': True, 'name': 'li_rm', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQH6WDDqB-iJDwAAAXe-mWlpCt-uZqnjKJlDBf9IKCWxmhbvcg3pFuddOLgZYHjgTLeENHykkaUWkBKANQ3yCGHLqAf3z3cXf3YT4yENhm9E9Ihy-1ndd01U'}]
#
#
# new_cookies = []
# for cookie in cookies:
#     #k代表着add_cookie的参数cookie_dict中的键名，这次我们要传入这5个键
#     for k in {'name', 'value', 'domain', 'path', 'expiry'}:
#         #cookie.keys()属于'dict_keys'类，通过list将它转化为列表
#         if k not in list(cookie.keys()):
#             #saveCookies中的第一个元素，由于记录的是登录前的状态，所以它没有'expiry'的键名，我们给它增加
#             if k == 'expiry':
#                 t = time.time()
#                 cookie[k] = int(t)    #时间戳s
#        #将每一次遍历的cookie中的这五个键名和键值添加到cookie
#     new_cookies.append({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
#
#
#
#
#
# # browser.add_cookie(cookies)
# # url2 = 'https://www.linkedin.com/in/eva-jiang-541b0186/'
# # browser.get(url2)
# #
# # browser.find_elements_by_xpath("//span[text()='加为好友']").click()
#
#
# # browser.find_element_by_xpath('//div[@id="global-nav-typeahead"]/div[1]/input').send_keys('sofa' + Keys.ENTER)
# # browser.find_element_by_xpath("//button[text()='会员']").click()
# # url = 'https://www.linkedin.com/search/results/people/?keywords=sofa&origin=SWITCH_SEARCH_VERTICAL&page=95'
# # browser.get(url)
# # time.sleep(5)
# # next_btn = browser.find_element_by_xpath('//span[ @class="artdeco-button__text"  and  text()="下页" ]')
#
# # while True:
# #     ss = browser.find_elements_by_xpath("//span[text()='加为好友']")
# #     print(ss)
# #     print(len(ss))
# #     # print(ss.count())
# #     # for i in ss:
# #     #     i.click()
# #     #     time.sleep(1)
# #     #     browser.find_elements_by_xpath("//span[text()='发送']")
# #     #     time.sleep(3)
# #
# #     next_btn = browser.find_element_by_xpath("//span[text()='下页']")
# #     if next_btn:
# #         print('挖掘下一页ing......')
# #         next_btn.click()
# #     else:
# #         break
# # print('end')
#
# # s = browser.get_cookies()
# #
# #
# # print(s)
#
#
# # browser.find_element_by_id('username').send_keys("18669319099")
# # browser.find_element_by_id('password').send_keys("liu8581393")
# # browser.find_element_by_class_name('login__form_action_container').click()


# import requests
#
# ret = requests.get("http://147.139.6.71:8080/get_mail/?website=https://senserussia.com/")
# print(ret.content.decode())
# from requests_html import HTMLSession
# session = HTMLSession()
# response = session.get('http://www.santostang.com/2018/07/04/hello-world/')
# #response.html.render(timeout = 60)
# print(type(response.html.render(timeout = 60)))
di = {28: 1, 6: 1, 22: 1, 8: 1, 44: 1, 17: 1}
r = sorted(di.items())
print(r)
