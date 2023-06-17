"""
模块的定义： 模块是一个 python 文件，以 .py 结尾包含了 Python 对象定义和 Python 语句
            之前引用过 random 模块，可以在 lib 文件夹下找到相应的文件
导入模块的方式：
    import 模块名 1
        模块定义别名：import 模块名 as 别名
    import 模块名 1, 模块名 2, ...(不推荐)
    from 模块名 import 功能 1, 功能 2, ...
    from 模块名 import *
        功能定义别名: from 模块名 import 功能 as 别名




"""
# import math
# print(int(math.sqrt(9)))

from math import sqrt
print(sqrt(9))

# import time as tt
# # 定义别名后就只能使用别名不能使用模块名了
# tt.sleep(2)
# print('hello')

from time import sleep as sl
sl(2)
print('hello')


