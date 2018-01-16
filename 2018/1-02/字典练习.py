
##字典练习

info={"qiudengkui":100,"qiushaowen":98,"qiuyangyang":97}
for i in info:
    print(info[i])
name=input("请输入你的姓名查询分数：")
ssd=info.get(name,"false")
if ssd == "false":
    print("你搜索的名字不存在，请检查后重试！")
else:
    x=info[name]
    print("%s,你的分数为：%s"%(name,x))
