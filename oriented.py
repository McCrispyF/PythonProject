class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name + "正在学习")

s = Student("张三")
s.study()