a = (1,2,3)
set(a)
print(a)

b = {'年龄' : 23,'身高' : 170}
print(b['年龄'])
print(b['身高'])

b['年龄']=24         ##给字典里的
print(b['年龄'])

'年龄'in b   #判断key是否在字典里，如果有返回True，如果没有返回False