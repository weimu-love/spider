# -*- coding: utf-8 -*-
"""
   File Name：     09-Save_mysql
   Description :    https://cuiqingcai.com/5578.html
   date：          2020/2/11
"""
import pymysql

# db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()

# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version: ', data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')

# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
#
# db.close()


# id = '20120001'
# user = 'Bob'
# age = 20
#
# db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     print('...')
#     db.rollback()
# db.close()

# 动态sql
db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('successful..')
        db.commit()
except:
    print('failed..')
    db.rollback()
db.close()
