# -*- coding: utf-8 -*-
"""
   File Name：     07-Save_json
   Description :
   date：          2020/2/11
"""
import json

# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))
# print(data[0]['name'])


# data = [{
#     'name': 'Bob',
#     'gender': 'male',
#     'birthday': '1992-10-18'
# }]
# # indent代表缩进字符数
# with open('data.json', 'w') as f:
#     f.write(json.dumps(data, indent=2))


# 如果包含中文
data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
# 为了输出中文，还需要指定参数ensure_ascii为False，另外还要规定文件输出的编码
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))
