#字典 dictionary dic dict
#键——值 key-value
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

customer={
    "nickname":"陈智仪",
    "age":18,
    "is_vip":False
}
#访问字典中的值
#print(customer["nickname"])

#get()
print(customer.get("age"))
print(customer.get("id","0000"))

#更新字典内容
customer["is_vip"] =True
print(customer)
