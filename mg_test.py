from pymongo import MongoClient

# 实例化
client = MongoClient(host="127.0.0.1", port=27017)
collection = client["mnt"]["t252"]

data_list = [{"_id": i, "name": "py{}".format(i)} for i in range(1000)]
collection.insert_many(data_list)
ret_cursor = collection.find()
ret_list = list(ret_cursor)
res_list = [i for i in ret_list if i["_id"] % 100 == 0 and i["_id"] != 0]
