#lambda function 匿名函数 只适用于简单函数 单行表达式  自动return  无法直接调用  通常作为高阶函数的参数使用

#定义 lambda 参数列表:函数体

out = lambda : print("aaa")

add = lambda x,y:x+y

out()
print(add(10,20))


data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript"]
data_list.sort(key = lambda item : len(item),reverse = True)
print(data_list)