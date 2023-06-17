# 定义all列表后只能导入列表里面的功能
__all__ = ['testA']


def testA(a, b):
    print(a + b)


# 测试信息
# 在本模块下__name__的值为__main__
# 不在本模块本调用时，__name__的值为当前模块的文件名
if __name__ =='__main__':
    testA(1, 1)


def testB():
    print('testB')


