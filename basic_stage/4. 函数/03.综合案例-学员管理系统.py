"""
需求（系统简介）：
    1.添加学员
    2.删除学员
    3.修改学员信息
    4.查询学员信息
    5.显示所有学员信息
    6.退出系统
    用户根据自己的需求来选取

步骤：
    1.添加功能界面函数
    2.搭建框架
    3.定义不同功能的函数

"""


def index():
    print("学员管理系统")
    print("请输入您要实现的功能：")
    print("1.添加学员")
    print("2.删除学员")
    print("3.修改学员信息")
    print("4.查询学员信息")
    print("5.显示所有学员信息")
    print("6.退出系统")
    print("-------")


students = []
# 定义一个空列表存储所有学员信息，每个学员应以字典的形式存储


def add_stu_info():
    """
    添加学员函数
    """
    new_stu_id = input("请输入学生学号：")
    new_stu_name = input("请输入学生姓名：")
    new_stu_tel = input("请输入学生电话：")
    global students

    for i in students:
        if new_stu_id == i['id']:
            print("该用户已经存在")
            return
            # return的作用是退出add_stu_info函数，后面添加学员的代码不执行

    # 判断完成，可以添加：定义一个新的学员，将用户输入的信息写入到新学员的信息中
    new_stu = {}
    new_stu['id'] = new_stu_id
    new_stu['name'] = new_stu_name
    new_stu['tel'] = new_stu_tel
    # 将新学员加入到所有学员中
    students.append(new_stu)
    print(students)


def del_stu_info():
    """
    删除学员函数
    """
    del_stu_id = input("请输入欲删除学员的学号：")
    global students
    for i in students:
        if del_stu_id == i['id']:
            students.remove(i)
            break
    else:
        print('该学员信息不存在')
    print(students)


def alter_stu_info():
    """
    修改学员函数
    """
    test_stu_id = input("请输入欲修改的学员学号: ")
    global students
    for i in students:
        if test_stu_id == i['id']:
            i['id'] = input("请输入学生学号：")
            i['name'] = input("请输入学生姓名：")
            i['tel'] = input("请输入学生电话：")
            break
    else:
        print("该学员信息不存在")
    print(students)


def search_stu_info():
    """
    查找学员函数
    """
    test_stu_id = input("请输入欲修改的学员学号: ")
    global students
    for i in students:
        if test_stu_id == i['id']:
            print(f"您所查找的学生学号是：{i['id']},姓名是：{i['name']},电话是：{i['tel']}")
            # 引号嵌套，外面必须是双引号，里面是单引号
            break
    else:
        print("学员不存在")


def see_stu_info():
    """
    查找全部学员函数
    """
    global students
    for i in students:
        print(f"学生的学号为：{i['id']}\t学生的姓名为：{i['name']}\t学生的电话为：{i['tel']}\t")


# 搭建学员管理系统框架
while True:  # 制造一个死循环，直到用户输入6后退出循环
    index()
    users_num = int(input("请您输入功能序号："))
    if users_num == 1:
        add_stu_info()
    elif users_num == 2:
        del_stu_info()
    elif users_num == 3:
        alter_stu_info()
    elif users_num == 4:
        search_stu_info()
    elif users_num == 5:
        see_stu_info()
    elif users_num == 6:
        result = input("确定要退出吗? yes or no? : ")
        if result == "yes":
            break
    else:
        print("您输入的功能序号有误")






