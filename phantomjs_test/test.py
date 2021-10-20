from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.PhantomJS()

'''
[{'domain': '.google.com', 'expires': 'Sat, 28 Aug 2021 06:48:06 GMT', 'expiry': 1630133286, 'httponly': True, 'name': 'NID', 'path': '/', 'secure': False, 'value': '210=MWG_fZWKaEIbO-EMJeCE9Uc_w6Pe20NvjkpQOhBMuC0hGR0P5eSoO-OadlhdsEyaOd5KIhT7XaamrNq2GDXZ-6YPDA7GTLsT0zP5UaO_dM6kxh-_WyACPUOkDexR35cqeihEMoBiupp5mhIg8p5y5OYHKhOSx11kTjzUBCArInc'}, {'domain': '.google.com', 'expires': 'Wed, 25 Aug 2021 06:48:06 GMT', 'expiry': 1629874086, 'httponly': True, 'name': 'CGIC', 'path': '/search', 'secure': False, 'value': 'Ij90ZXh0L2h0bWwsYXBwbGljYXRpb24veGh0bWwreG1sLGFwcGxpY2F0aW9uL3htbDtxPTAuOSwqLyo7cT0wLjg'}]

'''
browser.get('http://www.google.com/search?q=sofa')
browser.maximize_window()
browser.save_screenshot('a.png')
print(browser.page_source)

# browser.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]').click()

browser.get_cookies()
with open('test.html','w',encoding='utf-8') as f:
    f.write(browser.page_source)
