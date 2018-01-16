#集合的创建，需要一个list或者是一个字符串作为输入对象，把list或者是字符串转化为集合
#集合的特性：
#1：是一组key的集合，但不存储value
#2：由于key不能重复，所以，在set中，没有重复的key
#3：集合是无序的

x=set("qiun")
print(x)
y=set("deng")
print(y)

print("**"*20)


##集合的数学运算：

print(x,y)

print("1:集合的交集，两个集合共有的key")
print(x & y)
print("2:集合的并集，合并两个集合，除了重复的")
print(x | y)
print("2:集合的差集，集合1减去集合2共有的字符")
print(x - y)

s=set([1,2,3,4])
print(s)

s=set([1,2,3,4,1,2,3,6])  ##重复元素在集合中自动被过滤掉
print(s)

s.add(7)    ##添加一个元素，如何添加的元素和集合中的一样，没有什么效果
print(s)

s.remove(1)  ##删除一个元素
print(s)