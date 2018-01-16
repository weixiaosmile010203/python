#definition dictionaries(定义字典)
information={"name":"Chiudk","age":18,"height":171}

print(information)
#{'name': 'Chiudk', 'age': 18, 'height': 171}
print(information["name"])
#Chiudk
print(information["age"])
#18
print(information["height"])
#171
print("**"*20)


print("个人信息如下：\n姓名：%s\n年龄：%s\n身高：%s"%(information["name"],information["age"],information["height"]))
"""
个人信息如下：
姓名：Chiudk
年龄：18
身高：171
"""