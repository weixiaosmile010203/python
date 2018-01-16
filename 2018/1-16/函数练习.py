
def Menu():
    "打印出菜单选项，供用户选择"
    print("/*"*20)
    print("           信息管理系统V1.0          ")
    print("___________________________________")
    print("------>    1:添加用户信息  <--------")
    print("------>    2:查询用户信息  <--------")
    print("------>    3:更改用户信息  <--------")
    print("------>    4:删除用户信息  <--------")
    print("------>    5:所有用户信息  <--------")
    print("------>    6:退出系统  <--------")
    print("/*"*20)


def UserInput():
    "从用户哪里获取输入的序号"
    Num = input("请输入序号选择你想进行的操作：")
    if str.isdigit(Num) == True:   ##判断输入的类型是否为数字
        return int(Num)
    else:
        print("请输入数字序号！")

UserList = []
while True:
    Menu()
    GetUserInput = UserInput()
    if GetUserInput == 1:
        NewUser = input("请输入您的用户名：")
        if NewUser not in UserList:
            UserList.append(NewUser)
        else:
            print("输入的用户名已经存在，请输入其它用户名")

    elif GetUserInput == 2:
        SearchUser = input("输入你要查询的用户名：")
        if SearchUser in UserList:
            index = UserList.index(SearchUser)
            print(UserList[index])
        else:
            print("你查询的用户名不存在！")
    elif GetUserInput == 3:
        SearchUser = input("输入你要更改的用户名：")
        if SearchUser in UserList:
            index = UserList.index(SearchUser)
            SetUser = input("输入你想更改的用户名：")
            UserList[index] = SetUser
            print("已将用户名:%s更改为:%s"%(SearchUser,SetUser))
    elif GetUserInput == 4:
        SearchUser = input("输入你要删除的用户名：")
        if SearchUser in UserList:
            index = UserList.index(SearchUser)
            UserList.remove(SearchUser)
        else:
            print("你要删除的用户名不存在")
    elif GetUserInput == 5:
        for i in UserList:
            print(i)
    elif GetUserInput == 6:
        break
    else:
        print("您输入的有误，请检查！")

