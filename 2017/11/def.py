def printInfo():
	print("#"*30)
	print("家庭医生录入系统")
	print("1：添加信息")
	print("2: 删除信息")
	print("3: 修改信息")
	print("4：查看信息")
	print("#"*30)

printInfo()




userInfo = {}
inputInfo=int(input("请输入你的选择："))
if inputInfo == 1:
    name = input("请输入你的名字：")
    age = input("请输入你的年龄:")
    job = input("请输入你的职业：")

elif inputInfo == 2:
    pass
elif inputInfo == 3:
    pass
elif inputInfo == 4:
    pass
else:
    pass
