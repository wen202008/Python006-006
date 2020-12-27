学习笔记

基本数据类型：
整型:整数  intNum = 2
浮点型：带小数的数值 number=2.1
字符串：用2个单引号或双引号括起来的文本  str="I'm a string"
布尔值：表示真假，非真即假：True、False  bool=True
列表：包含多个字构成的序列，以[]来包含,表项之间用逗号分隔，可以用下标、切片、for循环取值. list=['one',1,2,'key']
元组：用()括起来的多个数据的序列，也用逗号分隔多个值   eggs=('hello',4,0.5)
字典：用{}括起来的键值对    dict={'key1':'value1',2:'two'}

控制流：
if判断,if后跟条件，然后冒号，然后下一行缩进执行代码块
if True:
	代码块
else：
	代码块
	
while：只要while语句条件为True，子句的代码就会执行
while True:
	代码块

for循环包含：for关键字，一个变量名，in关键字，冒号，从下一行开始缩进的代码块
for i in range(3):
	print(i)
  
用import导入模块
import re
re.match('[0-9]{11}','13912345678')  #匹配手机号码