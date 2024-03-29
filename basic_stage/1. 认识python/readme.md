# 认识Python
## 一、下载安装解释器与集成开发环境
### 安装解释器
什么是解释器？
通俗来讲，将我们所写的代码翻译成机器可以听的懂得语言的工具就是解释器  
解释器下载地址:  
``https://www.python.org/downloads/release/python-372/``  
进入网站后，依据需求下载即可： 
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/2023-06-17_110712.png)  
安装时选择 Add Python3.7 to Path  
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image.png)  
验证解释器是否安装成功——在cmd命令中输入python:  
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image%20(1).png)  
****
### 安装集成开发环境（IDE）
下载地址：``http://www.jetbrains.com/pycharm/download/#section=windows`` 下载社区版  
安装时选择：  
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image%20(2).png)  
安装完成后创建你的第一个项目：  
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image%20(3).png)  
这个开发环境会陪伴你很长时间，所以在编写你的第一句代码时，先修改一下界面外观吧！  
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image%20(4).png)   
![image](https://github.com/138470/Python_study/blob/main/basic_stage/1.%20%E8%AE%A4%E8%AF%86python/GitHub%20readme_picture/image%20(6).png) 
## 二、编写你的第一句代码
对这个充满魅力的世界献上最真诚的敬意！
```ruby
print('hello world')
```
## 三、认识数据类型
python中的数据类型有：
数值类型（int、float、bool）,&nbsp;字符串str,&nbsp;元组tuple,&nbsp; 列表list, &nbsp;字典dict,&nbsp; 集合set（不常用）

可变数据类型与不可变数据类型：  
    不可变的数据类型：数值型（int、float、bool）、字符串、元组  
    可变的数据类型：列表、字典、集合  
    可变是指该数据类型所对应的变量的值发生改变时，内存地址不发生改变

## 四、输入与输出
### 输入  

    input输入的特点:  
    
1.等待用户输入完成后才执行下一条命令  
2.要定义一个变量来接收用户输入的数据  
3.输入的任意的数据都当作``字符串``来处理，要进行数据类型转换  
    
    数据类型转换：要转换什么类型，就用什么类型的函数。例如：转换为整形 :int(a)

****
### 输出  
    1.格式化符号输出：  

整数格式输出 ：  
&nbsp;&nbsp;&nbsp;&nbsp;- 直接输出某个整数，直接用 f 语句  
&nbsp;&nbsp;&nbsp;&nbsp;- %0xd ——x表示输出的整数显示位数，不足的以0补全，超过的以原样输出 

浮点型格式输出 ：  
&nbsp;&nbsp;&nbsp;&nbsp;- 直接输出浮点型数据默认保留六位小数  
&nbsp;&nbsp;&nbsp;&nbsp;- %.xf x表示你要保留的小数位数 如：%2f-保留两位小数  

字符串格式输出 ：  
&nbsp;&nbsp;&nbsp;&nbsp;- 当输出的字符串中有特殊符号时，如'',要加转义符\,否则会报错  
&nbsp;&nbsp;&nbsp;&nbsp;- 字符串切片操作等  
        
    2.多个格式化输出  
照猫画虎即可  
    
    3.print语句：  
    
使用end来控制 print 以何种方式结束输出  
&nbsp;&nbsp;&nbsp;&nbsp;\n 换行符，print默认换行  
&nbsp;&nbsp;&nbsp;&nbsp;\t 制表符，带有对齐功能  

## 五、运算符与公共运算符  

    算术运算符：+ ,- , * , / , //(整除), %(取余), **(指数),()
除法"/"无论除数被除数是否为浮点型，其结果都为浮点型

    赋值运算符：“=”
多变量赋值，多变量赋相同值

    复合赋值运算符
+= ， -= ，*= ，/= 等算术运算符在赋值运算符前的复合赋值运算符
注意：先算复合赋值运算符右面的表达式再算复合赋值运算，见下方例子

    比较运算符
==(判断是否相等),>,<,!=（不等于）,>=（大于等于）,<=（小于等于）

    逻辑运算符
and且(都真为真，都假才假),  
or或(有一个为真就真，有一个为假就假),  
not非（取反）  
书写习惯： 在条件上加（）避免歧义，例如：print(（a > b） or （a > c）)


    公共运算符：
1.‘+’&nbsp;合并，适用于字符串、列表、元组  
2. ‘*’&nbsp; 复制，适用于字符串、列表、元组  
3.in/not in - 判断元素是否存在  
适用于字符串、元组、列表、字典


