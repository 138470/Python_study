"""
1.查找：找字串在字符串中的位置
find()检测某个字串是否包含在这个字符串中，如果有，返回字串开始位置的下标
index()用法与find一样。不过如果字串不存在，find返回-1，index报错
rfind(), rindex()用法与上述两个函数一样，只不过是从右侧开始查找

2.计数
count("要查找的子串", 开始位置下标, 结束位置下标)
"""
str1 = "dah abc def hello python and hello world"

print(str1.index("hello", 20, 50))  # 加了开始下标和结束下标就限制了查找范围
print(str1.find("ands"))  # 没有这个字串返回-1
print(str1.count("hello"))  # 查找hello字串的个数，没有则返回0

print("-------")
"""
3.修改字符串
replace("旧子串","新子串",替换的次数)

4.分割字符串，返回一个列表数据
split("分割符号", 分割次数)

5.合并列表里的字符串为一个大字符串
"连接符号".join(多字符串组成的序列)
"""
new_str1 = str1.replace("hello", "nihao", 1)
print(str1)
print(new_str1)

# 注意：
# replace函数并不是在原有的字符串上进行修改，而是带有一个返回值，需要定义一个新的变量来接受返回值
# 若替换次数大于子串出现的次数，则默认修改全部子串
list1 = str1.split("hello", 2)  # 分割后的结果会丢失hello符号
print(list1)

list2 = ["aa", "bb", "cc"]
new_str = "...".join(list2)  # 使用...来连接列表里的字符串
print(new_str)

print("-------")

"""
6.转换大小写(了解即可)
capitalize():将字符串的首字母转换为大写
title()：将字符串每个单词的首字母转换为大写
lower():将字符串中的所有的大写转小写
upper():将字符串中的所有的小写转大写

"""

str2 = "abc def ghi"
print(str2)
new_str2 = str2.capitalize()
print(new_str2)

new_str2 = str2.title()
print(new_str2)

new_str2 = str2.lower()
print(new_str2)

new_str2 = str2.upper()
print(new_str2)

print("-------")

"""
7.删除空白字符（了解）
lstrip()删除左侧空白字符；rstrip()删除右侧空白字符；strip()删除两侧空白字符

8.控制字符串对齐（了解）
左对齐：字符串序列.ljust(长度，填充字符)
右对齐：字符串序列.rjust(长度，填充字符)
居中对齐：字符串序列.center(长度，填充字符)

9.判断
判断是否以某个子串开头：字符串序列.startswith(子串，开始位置，结束位置)
判断是否以某个字串结尾：字符串序列.endswith(子串，开始位置，结束位置)
判断一个字符串中是否所有字符都为字母：isalpha()
判断一个字符串是否只包含数字：isdigit()
判断一个字符串是否为数字、字母或数字字母的组合：isalnum()
判断一个字符串是否都为空白：isspace()

"""
str3 = "hello122"
print(str3.ljust(10, "."))  # 控制字符串对齐
print(str3.isalpha())  # 有空格返回false
print(str3.isalnum())

