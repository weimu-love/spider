# -*- coding: utf-8 -*-
"""
   File Name：     requests
   Description :
   date：          2020/2/10
"""
import requests
import re
import logging

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)

# r = requests.get('http://httpbin.org/get')
# print(r.text)

# data = {
#     'name': 'germy',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get',params=data)
# print(r.text)


# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
#                   '80.0.3987.87 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)


# data = {'name': 'germy', 'age': 22}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)

# r = requests.get('http://www.jianshu.com')
# exit() if not r.status_code == requests.codes.ok else print('request successfully')


# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)


# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + "=" + value)


# headers = {
#     'cookie': '_zap=608b3fef-7691-47f4-905f-5b4dab92cde3; _xsrf=7736c509-98de-45c2-86e9-1244f85082d9; d_c0="AMDX6sDIyxCPTmIsY4njTJhkKKLk0wTK3h4=|1581333632"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581333671; capsion_ticket="2|1:0|10:1581334603|14:capsion_ticket|44:MmYyMzMyNjZlNGIyNDM4ODk2Y2JmMTM0YTRjNGQ0NDE=|5e76bdce7356e1f8aff0d5d6bcc3e44eea2fe32760f24882ecf9d11857035aae"; l_n_c=1; r_cap_id="M2VmZGYyZDgzY2ZkNDA1Y2JkNjRlMTVkNTJlODUxZDI=|1581334605|0f213fdc988f8436e026efc097dcb9bca09ea903"; cap_id="MDY2NDNkMTM3ZmVjNGI1NzkyYjAwNjgyOWMyN2FlM2E=|1581334605|d0e1f007f92dd25e548165bc374f7ae51e327ebf"; l_cap_id="YzNlZDg5ODRiODc2NDViNzk4YWI5NDc4ZDNhY2JjZjU=|1581334605|4307ec54418fadec14018f1fa7118b149406b947"; n_c=1; z_c0=Mi4xRnJkZUJ3QUFBQUFBd05mcXdNakxFQmNBQUFCaEFsVk5XSTR1WHdBc3RKQUU5VDBSRVU5bVA1WXh6V1k2dEpsZ3d3|1581334616|fbe7fb2ea1a32dfda5c601df8bf6ea100e542c45; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581334620; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1581334619|1581333632',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
#     'host': 'www.zhihu.com',
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(r.text)


# cookies = '_zap=608b3fef-7691-47f4-905f-5b4dab92cde3; _xsrf=7736c509-98de-45c2-86e9-1244f85082d9; d_c0="AMDX6sDIyxCPTmIsY4njTJhkKKLk0wTK3h4=|1581333632"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581333671; capsion_ticket="2|1:0|10:1581334603|14:capsion_ticket|44:MmYyMzMyNjZlNGIyNDM4ODk2Y2JmMTM0YTRjNGQ0NDE=|5e76bdce7356e1f8aff0d5d6bcc3e44eea2fe32760f24882ecf9d11857035aae"; l_n_c=1; r_cap_id="M2VmZGYyZDgzY2ZkNDA1Y2JkNjRlMTVkNTJlODUxZDI=|1581334605|0f213fdc988f8436e026efc097dcb9bca09ea903"; cap_id="MDY2NDNkMTM3ZmVjNGI1NzkyYjAwNjgyOWMyN2FlM2E=|1581334605|d0e1f007f92dd25e548165bc374f7ae51e327ebf"; l_cap_id="YzNlZDg5ODRiODc2NDViNzk4YWI5NDc4ZDNhY2JjZjU=|1581334605|4307ec54418fadec14018f1fa7118b149406b947"; n_c=1; z_c0=Mi4xRnJkZUJ3QUFBQUFBd05mcXdNakxFQmNBQUFCaEFsVk5XSTR1WHdBc3RKQUU5VDBSRVU5bVA1WXh6V1k2dEpsZ3d3|1581334616|fbe7fb2ea1a32dfda5c601df8bf6ea100e542c45; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581334620; KLBRSID=9d75f80756f65c61b0a50d80b4ca9b13|1581334619|1581333632'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
#     'host': 'www.zhihu.com',
# }
# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get('http://www.zhihu.com', cookies=jar, headers=headers)
# print(r.text)


# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)


# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)


proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
requests.get('https://www.taobao.com', proxies=proxies, timeout=1)
