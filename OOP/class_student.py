### 练习 1：学生类
# 定义 `Student` 类，包含：
# - 姓名
# - 学号
# - 成绩列表
# 方法要求：
# - 添加成绩
# - 计算平均分
# - 打印学生信息
# 扩展要求：
# - 平均分为空时如何处理
# - 增加“是否及格”的方法

class Student:
    def __init__(self, name, student_id, score_list=[]):
        self.name = name
        self.student_id = student_id
        self.score_list = score_list

    def add_score(self, score=[]):   #往成绩列表添加成绩
        for i in score:
            self.score_list.append(i)
            print(f"成功添加成绩：{i}")

    def avg_score(self):
        sum_score = 0
        for s in self.score_list:
            sum_score += s
        if len(self.score_list) == 0:
            return 0.0
        elif len(self.score_list) != 0:
            return sum_score / len(self.score_list)

    def if_qualified(self):
        if int(self.avg_score()) >= 60:
            print("是否及格：是 (True)")
        else:
            print("是否及格：否 (False)")

    def print_student(self):
        print(f"学生信息：[学号：{self.student_id}] {self.name}，当前录入{len(self.score_list)}门成绩，平均分：{self.avg_score()}")

#测试1
roman = Student("Roman","A202601")
roman.add_score([85,92,78])
print(f"{roman.name}的平均分是：{roman.avg_score()}")
roman.if_qualified()
roman.print_student()

#测试2
roman = Student("李四","B202602")
roman.add_score()
print(f"{roman.name}的平均分是：{roman.avg_score()}")
roman.if_qualified()
roman.print_student()

#测试3
roman = Student("王五","C202603")
roman.add_score([40, 55])
print(f"{roman.name}的平均分是：{roman.avg_score()}")
roman.if_qualified()