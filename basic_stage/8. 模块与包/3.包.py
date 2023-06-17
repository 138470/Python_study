"""
将有联系的模块组织在一起，即放在同一个文件夹下，并且在这个文件夹创建一个名为__init__.py文件，这个文件夹就称为包
导入包的方法：
    1.import 包名.模块名
      包名.模块名.功能
    2.from 包名 import *
      模块名.目标
    使用这种方法时必须要先在包中的__init__文件中设置__all__列表以表明允许导入的模块
    不添加__all__列表会报错，无法导入任何模块
"""
import Mypackage.mymodule1
Mypackage.mymodule1.info_print()

from Mypackage import *
mymodule2.info_print()