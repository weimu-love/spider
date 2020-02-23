# -*- coding: utf-8 -*-
"""
   File Name：     13-Splash
   Description :    使用docker启动splash：  docker run -p 8050:8050 scrapinghub/splash
                    http:8050  https:8051  telnet:5023

                    如果docker报内存不够错误： https://segmentfault.com/q/1010000017575763?utm_source=tag-newest
                    注：会清空docker
                    使用教程： https://cuiqingcai.com/5638.html
   date：          2020/2/12
"""
import requests

# render.html
# url = 'http://localhost:8050/render.html?url=https://www.baidu.com'

# 此接口还可以指定其他参数，比如通过wait指定等待秒数。如果要确保页面完全加载出来，可以增加等待时间
# url = 'http://localhost:8050/render.html?url=https://www.taobao.com&wait=5'
# response = requests.get(url)
# print(response.text)

# render.png
# url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
# response = requests.get(url)
# with open('taobao.png', 'wb') as f:
#     f.write(response.content)


# render.har
# 此接口用于获取页面加载的HAR数据
# curl http://localhost:8050/render.json?url=https://httpbin.org

# 返回的JSON结果会含网页源代码和HAR数据
# curl http://localhost:8050/render.json?url=https://httpbin.org&html=1&har=1


# execute
# 此接口可实现与Lua脚本的对接

from urllib.parse import quote

# lua = '''
# function main(splash)
#     return 'hello'
# end
# '''


# lua = '''
# function main(splash, args)
#   local treat = require("treat")
#   local response = splash:http_get("http://httpbin.org/get")
#     return {
#     html=treat.as_string(response.body),
#     url=response.url,
#     status=response.status
#     }
# end
# '''
# url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
# response = requests.get(url)
# print(response.text)
