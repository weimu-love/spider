# -*- coding: utf-8 -*-
"""
   File Name：     10-Save_mongo
   Description :    https://cuiqingcai.com/5584.html
   date：          2020/2/11
"""
import pymongo

# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.test
collection = db.students

# 插入
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
# result = collection.insert_one(student)
# result = collection.insert_many([student1, student2])
#
# print(result)
# print(result.inserted_ids)


# 查询
# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)

# 根据ObjectId来查询
from bson.objectid import ObjectId

# result = collection.find_one({'_id':ObjectId('5e435ecf918464746eb2e00e')})
# print(result)

# 多条数据的查询
# results = collection.find({'age': 20})

# 查询年龄大于20的数据
# results = collection.find_one({'age': {'$gt': 20}})

# 正则匹配查询
# results = collection.find({'name': {'$regex': '^M.*'}})
# print(results)
# for result in results:
#     print(result)


# 计数
# count = collection.find().count()
# print(count)

# 偏移
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])

# 当数据量较大时，不适用偏移skip()
# from bson.objectid import ObjectId
# collection.find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}})


# 更新
condition = {'name': 'Mike'}
student = collection.find_one(condition)
student['age'] = 25

# 全部用student字典替换
# result = collection.update(condition, student)

# 只更新student字典内存在的字段
# result = collection.update(condition, {'$set': student})

# 用法更加严格，它们的第二个参数需要使用$类型操作符作为字典的键名
# result = collection.update_one(condition, {'$set': student})

# 返回结果是UpdateResult类型。然后分别调用matched_count和modified_count属性，可以获得匹配的数据条数和影响的数据条数
# print(result.matched_count, result.modified_count)

# 年龄加一
# result = collection.update_one(condition, {'$inc': {'age': 1}})
#
# print(result)




# 删除
result = collection.remove({'name': 'Kevin'})
print(result)


result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)


result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)