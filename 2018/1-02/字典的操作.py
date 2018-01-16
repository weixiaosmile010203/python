
information={"name":"Chiudk","age":18,"height":171}
print(information)

information["weight"]=67   ##1:往字典里面添加键值对，添加元素
print(information)
print(information["weight"])


information["name"]="leslie"   ##2:字典中如果已经有了这个键，添加等于重新赋值了。把前面的抵消掉。
print(information)


#print(information["sex"])  ##3:在字典中调用时，如果key不存在，或报错。

#如果不确定key是否存在字典中，可以使用下面方式去确认
#"sex" in information    #(1)：通过in去判断是否存在

info=information.get("sex")  #(3.1):使用字典提供的get（）方法判断是否存在，不存在返回空
print(info)

info=information.get("age")  #(3.2):找到的话返回具体的值
print(info)

info=information.get("sex","没有找到你要查找的信息") #(3.3)为空时可以指定具体返回的内容
print(info)



print("*****"*10)
print(information)
#4:删除一个key，key删除了，value自然也就没有了
information.pop("name")
print(information)