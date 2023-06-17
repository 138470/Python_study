"""
一、面向对象三大特性
    1.封装
        将属性和方法书写到类里面的操作即为封装
        封装可以为某些属性和方法添加私有权限
    2.继承
        子类默认继承父类的所有属性和方法
        子类可以重写父类的属性和方法
    3.多态
        传入的对象不同，产生不同的结果
            调用不同子类对象的相同父类方法，可以产生不同的执行结果
二、类属性和实例属性
    类属性就是类对象所拥有的属性，他被该类所创建的所有实例对象共有
    类属性可以使用类对象或者实例对象访问
    类属性为全类共有，仅占用一份内存，更省空间
    修改类属性：
        通过类来修改
        通过实例对象修改 - 创建一个同名属性
三、类方法和静态方法
    1.类方法：
        使用装饰器 @classmethod 来标识类方法
        类方法通常是用来访问类属性或者修改类属性的
    2.静态方法：
        使用装饰器 @staticmethod 来标识静态方法
        静态方法既可以使用对象访问也可以使用类访问

"""
# 多态的实现步骤(需求：警务人员和警犬一起工作)：
# 定义父类（狗类和人类），并提供公共方法
# 定义子类（缉毒犬和追击犬），重写父类方法
# 传递子类对象给调用者，可以看到不同子类执行效果不同


# 体验多态
class Dog(object):
    tooth = 20

    def work(self):
        print('指哪打哪')


class A_Dog(Dog):
    def work(self):
        print('追击敌人')


class B_Dog(Dog):
    def work(self):
        print('追查毒品')


class Person(object):
    def work_with_dog(self, dog):
        dog.work()


wangcai = Dog()
xiaohei = Dog()
ad = A_Dog()
bd = B_Dog()
daqiu = Person()
daqiu.work_with_dog(bd)

print(Dog.tooth)
print(xiaohei.tooth)
print('-'*10)
# 修改类属性
Dog.tooth = 30
print(xiaohei.tooth)
xiaohei.tooth = 40
print(xiaohei.tooth)
print(wangcai.tooth)
print('-'*10)


# 体验类方法
class Dog(object):
    __tooth = 10

    # 定义类方法
    @classmethod
    def get_tooth(cls):  # cls 代表某个类
        return cls.__tooth

    @staticmethod
    def info_print():
        print('这是Dog类中的静态方法')


xiaohuang = Dog()
print(xiaohuang.get_tooth())
Dog.info_print()
xiaohuang.info_print()
