"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
展示全部学生成绩：展示出系统中所有学生的成绩
"""

class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        total = self.chinese + self.math + self.english
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{total}"

    #修改成绩类
    def update_score(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


class EduManagement:
    system_version = "1.0.1"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生的姓名：")

        for i in self.student_list:
            if i.name == name:
                print("学生已存在")
                return
        try:
            chinese = int(input("请输入学生的语文成绩："))
            math = int(input("请输入学生的数学成绩："))
            english = int(input("请输入学生的英语成绩："))
        except ValueError:
            print("输入错误，请输入数字")
            return

        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print(f"学生{name}信息添加成功")
        else:
            print("各科成绩必须在0-100之间")

    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                print(f"当前成绩：{i}")
                try:
                    chinese = int(input("请输入修改后的语文成绩："))
                    math = int(input("请输入修改后的数学成绩："))
                    english = int(input("请输入修改后的英语成绩："))
                except ValueError:
                    print("输入错误，请输入数字")
                    return
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    i.update_score(chinese,math,english)
                    print(f"学生{name}信息修改成功")
                    print(f"修改后的成绩：{i}")
                    return
                else:
                    print("各科成绩必须在0-100之间")
                    return
        print("未找到该学生")

    #删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                print("学生信息删除成功")
                return
        print("未找到该学生")

    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                print(i)
                return
        print("未找到该学生")

    #展示全部学生成绩
    def list_show(self):
        if not self.student_list:
            print("没有学生")
            return
        for i in self.student_list:
            print(i)

    #运行系统
    def run(self):
        print(f"欢迎使用教务系统v{EduManagement.system_version}")
        menu= ("""
        ********************************
        *       1.添加学生              *
        *       2.修改学生              *
        *       3.删除学生              *
        *       4.查询指定学生           *
        *       5.查询所有学生           *
        *       6.退出系统              * 
        ********************************
        """)

        while True:
            print(menu)
            try:
                choice = int(input("请选择要进行的操作(1-6)："))
                match choice:
                    case 1:
                        self.add_student()
                    case 2:
                        self.update_student()
                    case 3:
                        self.delete_student()
                    case 4:
                        self.query_student()
                    case 5:
                        self.list_show()
                    case 6:
                        break
                    case _:
                        print("输入错误,请输入1-6的数字")
            except ValueError:
                print("输入错误，请输入数字")

edu = EduManagement()
edu.run()