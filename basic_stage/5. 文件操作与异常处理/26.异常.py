"""
异常语句 - 尝试运行可能会出现错误的代码，一旦发现错误就会执行其他的代码
    1.捕获异常的语法：
        try:
            可能发生错误的代码
        except 异常类型（可以有多个）:
            如果出现异常执行的代码
        else:
            如果没有异常要执行的代码
        finally:
            无论是否异常都要执行的代码
    Exception 是程序异常类的父类，不知道错误类捕型的情况下，可以用Exception代替

   2.异常传递：
        实现如下需求：
            1.以只读模式打开 text2 文件，文件不存在则给出提示信息
            2.循环读取内容，如果程序异常中止则给出提示信息

   3.自定义异常：
        自定义异常类，继承Exception，使用魔法方法设置异常描述信息



"""

# 体验异常捕获
try:
    print(num)
except (NameError, ZeroDivisionError) as result:
    print(result)

# 注意：
# 1.如果尝试执行的代码的异常类型和捕获的异常类型不一致，则无法捕获异常
# 2.try下面只放一行尝试执行的代码
# 3.Exception是程序异常类的父类，不知道错误类型的情况下，可以用Exception代替

try:
    f = open('test1', 'r')
except Exception:
    f = open('text1', 'w')
else:
    print('没有异常，很开心')
finally:
    f.close()

# 体验异常传递
# 需求：
# 1.以只读模式打开 text2 文件，文件不存在则给出提示信息
# 2.循环读取内容，如果程序异常中止则给出提示信息
import time
try:
    f = open('text2', 'r')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            # 导入time模块，使得每次打印间隔2s
            time.sleep(2)
            print(con)
    except:
        # 在cmd命令中,输入 py + 文件名（可以用tab键自动生成） ,按CTRL+C终止程序
        print('该程序被异常终止')
except:
    print('该文件不存在')


# 体验自定义异常
# 实现如下需求：密码长度不足则报异常
class Diy_error(Exception):
    def __init__(self, input_len, min_len):
        self.length = input_len
        self.min_len = min_len

    # 设置异常描述信息
    def __str__(self):
        return f'您输入的密码长度为{self.length},密码不能少于{self.min_len}'

def main():
    try:
        pwd = input('请输入您的密码： ')
        if len(pwd) < 3:
            # 抛出异常类创建的对象,可以理解为print，抛出的是str魔法方法
            raise Diy_error(len(pwd),3)
    # 捕获异常
    except Exception as result:
        print(result)

    else:
        print('密码已经输入完成')


main()
