"""
一、文件操作的步骤：
    1.文件打开 open(带路径的文件名, '访问模式')
        主访问模式：
            r - 只读
                文件不存在会报错
                文件指针在开头，写入内容也会报错
                拓展：
                    rb 二进制格式打开
                    r+ 可读可写
                    rb+ 二进制可读可写
            w - 只写
                文件不存在自动新建文件
                文件指针位置在开头，执行写入会覆盖原有内容
                拓展：
                    wb 二进制格式打开
                    w+ 可读可写
                    wb+ 二进制可读可写
            a - 追加
                文件不存在自动新建文件
                文件指针在末尾，执行写入在原有内容基础上追加新内容
                拓展：
                    ab 二进制格式打开
                    a+ 可读可写
                    ab+ 二进制可读可写
        访问模式可以省略，若省略默认访问模式为 'r'

    2.文件读写
        使用seek函数改变文件指针位置
            seek(偏移量，起始位置) - 起始位置为0表示开头，1表示当前位置，2表示结尾
        读：
        read(num) - num表示从文件中读取的数据长度，不写num默认读取所有数据
        readlines() - 按照行的方式一次性读取全部内容，并返回一个列表，每一行的内容为列表的一个元素
        readline() - 一次性读取一行的内容，第n次调用打印第n行
        写：
        write()
    3.关闭close()
    4.文件重命名与文件删除：
        rename(源文件名， 新文件名) - 重命名
        remove(文件名) - 删除文件
        重命名和删除文件操作都需要导入 os 模块

二、文件备份的步骤：
    1.规划文件名
    2.拆解文件名，将后缀前的文件名提取出来，拼接备份说明并组成新的文件名。
        提取方法：找到最后一个'.'
    3.备份文件写入数据，源文件以rb模式打开，备份文件以wb模式打开

三、文件夹操作：
    1.创建文件夹 - os.mkdir('文件夹名')
    2.删除文件夹 - os.rmdir('文件夹名')
    3.获取‘当前’文件的目录路径 - print(os.getcwd())
    4.改变目录路径 - os.chdir('欲修改的默认文件路径')
    5.获取目标文件夹下的所有文件，返回一个列表 - os.listdir('文件夹')
    6.重命名文件夹 - os.rename('源文件夹名', '修改后的文件夹名')

"""
# r 访问模式测试
# text写入内容abc123
f = open('text.txt', 'r')  # 以只读模式打开，文件不存在会报错
print(f.read())  # abc123
f.close()

f = open('text.txt', 'r+')  # 以r+模式打开，文件不存在会报错
f.write('456')  # 文件指针在开头，456会覆盖掉abc,text文件内容为 456123
f.seek(3, 0)
print(f.read(2))
f.close()
# 尽量不要在一个open中同时又读又写

f = open('text.txt', 'r+')  # 以r+模式打开，文件不存在会报错
print(f.read(3))  # 文件指针在开头，text文件内容为 456123,打印456
f.close()

f = open('text.txt', 'r')
print(f.read())  # 456123
f.close()
print('-'*10)

# w 访问模式测试
# text 文件写入456123
f = open('text.txt', 'w')  # w 访问模式，文件不存在会直接创建新文件,读取文件操作会报错
f.write('abc')  # 文件指针从开头开始，text文件内容变为abc,覆盖掉456123
f.close()

f = open('text.txt', 'w+')
f.write('cba')  # 文件指针从开头开始，text文件内容变为cba,覆盖掉abc
f.close()

f = open('text.txt', 'r')
print(f.read())  # 文件指针从开头开始，text文件内容变为cba,覆盖掉abc
f.close()

f = open('text.txt', 'w+')
print(f.read())  # 文件指针从开头开始，空内容会覆盖掉所有，text文件内容为空
f.close()

# a 访问模式测试
# 写入内容abc123
f = open('text.txt', 'w+')
f.write('abc123')
f.close()

f = open('text.txt', 'a')  # a 访问模式，文件不存在会直接创建新文件,读取文件会报错
f.write('456')  # 文件指针在末尾，追加后文件内容为：abc123456
f.close()

f = open('text.txt', 'a+')
print(f.read())  # 文件指针在末尾，控制台打印空内容
f.close()

f = open('text.txt', 'r')
print(f.read())  # abc123456

# 测试完毕，回到初始状态abc123
f = open('text.txt', 'w')
f.write('abc123')
f.close()

# readlines 测试
f = open('test1.txt', 'r')
print(f.readlines())  # ['aaaaa\n', 'bbbb\n', 'ccc\n', 'dd\n', 'e']

# readline 测试
f = open('test1.txt', 'r')
print(f.readline())  # aaaaa 第一次调用打印第一行
print(f.readline())  # bbbb 第二次调用打印第二行


# 文件备份测试
# 规划文件名
old_file_name = input('请输入您要备份的数据的文件名：')
# 拆解文件名，将后缀前的文件名提取出来，拼接备份说明并组成新的文件名。
# 提取方法：找到最后一个'.'
site = old_file_name.rfind('.')

# 分析用户输入的文件名，有效的文件名才会备份
if site > 0:
    new_file_name = old_file_name[0:site] + '[备份]' + old_file_name[site:]
else:
    print('您输入的文件名不合法')

# 备份文件写入数据
# 源文件以rb模式打开，备份文件以wb模式打开
old_f = open(old_file_name, 'rb')
new_f = open(new_file_name, 'wb')

while True:
    result = old_f.read(1024)  # 读取1024位即1kb内存
    if len(result) == 0:
        break
    new_f.write(result)

""" 文件夹操作："""
import os

# 1.rename(源文件名， 新文件名) - 重命名
# os.rename('1.txt', '10.txt')
#
# 2.remove() - 删除文件
# os.remove('10.txt')

# 创建文件夹
# os.mkdir('aa')

# 删除文件夹
# os.rmdir('aa')

# 获取 当前 文件的目录路径
# print(os.getcwd())

# 改变目录路径
# os.mkdir('aa')
# os.chdir('aa')
# os.mkdir('bb')

# 获取目标文件夹下的所有文件，返回一个列表
# print(os.listdir('aa'))

# 重命名文件夹
# os.rename('aa', 'bbbb')







