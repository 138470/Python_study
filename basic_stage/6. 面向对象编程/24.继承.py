"""
继承 - 指的是多个类之间的所属关系，子类默认继承父类的所有属性和方法
    1.单继承：一个子类只继承一个父类

    2.多继承：一个子类同时继承了多个父类
        当多个父类拥有同名属性和方法的时候，优先继承第一父类的同名属性和方法

        子类重写父类同名方法和属性：
            子类和父类拥有同名属性和方法，子类创建对象调用同名属性和方法的时候，调用到的是子类里面的同名属性和方法

        子类调用父类的同名属性和方法：
            方法一：将父类方法写入子类，并规范好初始值
            方法二：super()调用父类方法 - 自动查找父类，顺序遵循mro层级顺序
    3.多层继承

    4.私有属性和方法
        某些属性或方法不继承给子类
        设置权限的方法：在属性名和方法名之前加上两个下划线 __
        获取和修改私有属性值 - 只能在类里面修改
            获取：get_xx()  修改：set_xx()
"""


# 体验继承
# 定义一个父类A
class A(object):  # 所有类默认继承基类（顶级类） object,除了基类所有子类也称派生类
    # 定义这个类的初始属性
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# B继承A的所有属性和方法
class B(A):
    pass


result = B()
result.info_print()
print('-' * 10)


# 体验多层继承
# 定义师傅类
class Master(object):
    def __init__(self):
        self.recipe = '[古法煎饼果子配方]'
        self.__money = 10000

    def make_cake(self):
        print(f'运用{self.recipe}制作煎饼果子')

    # 获取私有属性
    def get_money(self):
        return self.__money

    # 修改私有属性
    def set_money(self):
        self.__money = 20000


# 定义学校类
class School(object):
    def __init__(self):
        self.recipe = '[学校煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.recipe}制作煎饼果子')


# 定义徒弟类 prentice, 继承师傅类和学校类
class Prentice(School, Master):
    def __init__(self):
        self.recipe = '[独门煎饼果子配方]'

    def make_cake(self):
        self.__init__()
        # 加入自己初始化的原因：recipe的属性值是上一次调用的init内的recipe属性值
        print(f'运用{self.recipe}制作煎饼果子')
        # super().__init__()
        # super().make_cake()

    def make_old_cake(self):
        print(f'运用{self.recipe}制作煎饼果子')
        super().__init__()
        super().make_cake()

    # 在子类中调用父类方法
    def make_Master_cake(self):
        Master.__init__(self)
        # 如果不加Master的初始化方法，self.recipe的值为‘[独门煎饼果子配方]’
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)
        # 如果不加Master的初始化方法，self.recipe的值为‘[独门煎饼果子配方]’
        School.make_cake(self)

    def __info_print(self):
        print('这是私有方法')


# 定义徒孙类
class Tusun(Prentice):
    def __init__(self):
        self.money = 20

    def make_old_cake(self):
        # 找到当前子类的上一父类的方法，有两个父类默认找第一父类
        super().__init__()
        super().make_old_cake()


# 创建徒弟对象lzp
lzp = Prentice()
lzp.make_cake()  # 子类与父类中都有 make_cake方法, 对象调用make_cake方法时，调用的是子类方法。
# 运用[独门煎饼果子配方]制作煎饼果子
print(Prentice.__mro__)  # 继承层级顺序
# (<class '__main__.Prentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)
print('-' * 10)


# 子类调用父类的属性和方法 - 将父类方法写进子类方法中，并且规范初始值
lzp.make_Master_cake()  # 运用[古法煎饼果子配方]制作煎饼果子
lzp.make_School_cake()  # 运用[学校煎饼果子配方]制作煎饼果子
lzp.make_cake()  # 运用[独门煎饼果子配方]制作煎饼果子
print('-' * 10)


# super()调用父类方法 - 一次性调用两个父类方法
little_zp = Tusun()
little_zp.make_old_cake()
# 运用[独门煎饼果子配方]制作煎饼果子
# 运用[学校煎饼果子配方]制作煎饼果子
print('-' * 10)


# 多层继承
little_zp.make_School_cake()  # 使用徒弟类的方法
# 运用[学校煎饼果子配方]制作煎饼果子
print('-' * 10)


# 体验私有属性和方法
print(little_zp.money)
print(lzp.get_money())
lzp.set_money()
print(lzp.get_money())
