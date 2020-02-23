# -*- coding: utf-8 -*-
"""
   File Name：     08-Save_csv
   Description :
   date：          2020/2/11
"""
import csv

# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     # writer.writerow(['10001', 'Mike', 20])
#     # writer.writerow(['10002', 'Bob', 22])
#     # writer.writerow(['10003', 'Jordan', 21])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


# 爬取数据为字典时的写入方式
# with open('data.csv','w') as f:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(f,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
#
# # 追加数据
# with open('data.csv', 'a') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})

# 使用csv读数据
with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)