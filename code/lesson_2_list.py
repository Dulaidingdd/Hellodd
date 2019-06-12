favorite_fruit1 ="pear"
favorite_fruit2 ="grape"
favorite_fruit3 ="banana"

#列表_list
favorite_fruits =["pear","grape","banana"]
#print(favorite_fruits)

#列表也可存放不同的类型
#favorite_fruits =["pear","grape","banana",189,True]

#索引_ndex
# 访问列表中的某一元素
#favorite_fruits =["pear","grape","banana"]
#                   0        1        2
#                   -3     -2        -1
print(favorite_fruits[1])
print(favorite_fruits[-2])

#切片 slice
print(favorite_fruits[1:])
print(favorite_fruits[0:2])

#修改列表中的元素
favorite_fruits =["pear","grape","banana"]
favorite_fruits[1]="apple"
print(favorite_fruits)

#列表函数 listFunction
# extend 两个列表相加
my_food=["apple","pear","banana"]
my_number=[1,2,3,4,5]
my_food.extend(my_number)
print(my_food)

#append 把一个元素插入到列表最后
my_food.append("grape")
print(my_food)

#insert 把一个元素插入列表中任意位置
my_food.insert(0,"grape")
print(my_food)

#remove 把一个元素删除
my_food.remove("pear")
print(my_food)

#clear 清空列表中所有元素
my_food.clear()
print(my_food)

#pop 清理最后或指定位置元素
print(my_food)
my_food.pop(0)
print(my_food)

#index 确认某个元素是否在列表里
print(my_food)
print(my_food.index("banana"))

#count 查找列表中某个值元素的个数
my_food =["apple","apple","pear","peat","orange"]
print(my_food.count("apple"))

#sort 排序
my_food=["apple","pear","banana"]
my_number=[5,2,1,4,3]
my_number.sort()
print(my_number)

#reverse 反转
print(my_food)
my_food.reverse()


#copy 拷贝
my_food2=my_food.copy()

