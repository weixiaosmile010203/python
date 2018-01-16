#函数的定义：def 后面加上函数名字（）：

def functionName():
    print("函数内执行的内容")



def destriptionDocument():
    "说明文档直接写在这里，这样在使用help（函数名的时候，就会打印出函数的说明用途了！）"
    pass  #pass在函数没有写功能的时候起到一个占位的作用，为空时会报错
help(destriptionDocument)
