#str
s = 'ABCDEFG'
print(s[-1]) # G
print(s[-2]) # F
print(s[0:-1]) #ABCDEF
print(s[:]) #ABCDEFG
print(s[4:1:-1]) #EDC
print(s[0:4:2]) #AC
print(len(s)) #7
ret9 = 'title,Tilte,atre,'.split('t')
print(ret9) #['', 'i', 'le,Til', 'e,a', 're,']
#list
t = list([1,2,'3'])
print(t) # [1, 2, '3']
print(t.__len__()) # 3
t.append(3)
print(t) # [1, 2, '3', 3]
t.extend([4])
print(t) #[1, 2, '3', 3, 4]
t.append([5])
print(t) # [1, 2, '3', 3, 4, [5]]
t.insert(3,1)
print(t) #[1, 2, '3', 1, 3, 4, [5]]
t.insert(4,['a'])
print(t) # [1, 2, '3', 1, ['a'], 3, 4, [5]]
print('-----------------------')
#删除
#t.clear(); 清空list
print(t.count(1)) #2 计算某个字符出现的次数
a = t.copy();
print(a) #[1, 2, '3', 1, ['a'], 3, 4, [5]]
b = t.remove(1)
print(t) #[2, '3', 1, ['a'], 3, 4, [5]] 删除object第一次出现的元素
print(b) #None 由输出知是没有返回值的
t.pop(0)
print(t) #['3', 1, ['a'], 3, 4, [5]] 根据角标删除元素
del t[1]
print(t) #['3', ['a'], 3, 4, [5]]
#del t['3'] # 报错
t[0] = 1
print(t) # [1, ['a'], 3, 4, [5]]
c = t.index(['a'])
print(c) #1
#d = t.index(0) #index查找不到会报错 同str
t.clear()
t.extend([5,2,1,3,6,4])
t.sort() #排序 排序时只允许有一种数据类型
print(t) #[1, 2, 3, 4, 5, 6]
t.clear()
t.extend(['5','2','1','6'])
t.sort()
print(t) # ['1', '2', '5', '6']
t.append(3)
print(t) #['1', '2', '5', '6', 3]
t.reverse()
print(t) # [3, '6', '5', '2', '1']
#元组 跟list相同 tuple
tuple
#字典 dict
dict
d= dict({'a':'b'})
print(d) # {'a': 'b'}
print(type(d)) # <class 'dict'>
print(d.get('a')) # b
print(d['a']) #b
d.setdefault(1,2)
print(d) #{'a': 'b', 1: 2}
print(d) # {'a': 'b', 1: 2}
d['a'] = 'c'
print(d) #{'a': 'c', 1: 2}
dic_pop = d.pop('a')
print(dic_pop) # c
print(d) # {1: 2}
d = {1:3}
print(d) #{1: 3}
d.update()
item = d.items()
print(item) # dict_items([('a', 'b'), (1, 2)])
print(item,type(item)) # dict_items([(1, 3)]) <class 'dict_items'>
keys = d.keys()
print(keys,type(keys)) # t_keys([1]) <class 'dict_keys'>
values = d.values()
print(values,type(values)) #dict_values([3]) <class 'dict_values'>
d = {1:'a',2:2,3:3,'4':'4'}

for key in d:
    print(key) # 1 2 3 4
for key,value in d.items():
    print(key,value) # 1 a 2 2 3 3 4 4
for item in d.items():
     print(item) # (1, 'a')(2, 2)(3, 3)('4', '4')
msg = 'abcdefg'
#for 循环
for m in msg:
    print(m) # a ---g
#枚举 enumerate
li = [1,2,3,4,5,6,'7']
for i in enumerate(li):
    print(i) #(0, 1)(1, 2)(2, 3)(3, 4)(4, 5)(5, 6)(6, '7')
#range 随机
for i in range(1,10,2):
    print(i)
#id id是内存地址
print(id(1)) #8791266677792
#is 比较的内存地址 ==比较的数值
# python中pass的意义 1 空语句 do nothing 2 保证格式完整 3 保证语义完整
#python 有5中标准的数据类型 Number(数字) String(字符串) List(列表) Tuple(元组) Dictionary(字典)
# python支持不同的4中数字类型 int(有符号整型) long长整型(也可表示八进制和十六进制) float(浮点型) complex(复数)
# 加号（+）是字符串连接运算符，星号（*）是重复操作
# 元组相当于只读列表 元素不能二次赋值
# repr(x) 将对象 x 转换为表达式字符串
# chr(x) 将一个整数转换为一个字符
# oct(x) 将一个整数转换为一个八进制字符串
# hex(x) 将一个整数转换为一个十六进制字符串
# ord(x) 将一个字符转换为它的整数值
# unichr(x) 将一个整数转换为Unicode字符
import math
print(dir(math))
print(dir(str))
#可更改(mutable)与不可更改(immutable)对象
#在python中，strings, tuples, 和numbers是不可更改的对象，而 list,dict 等则是可以修改的对象。
#不可变类型：变量赋值a=5后再赋值a=10，这里实际是新生成一个int值对象10，再让a指向它，而5被丢弃，不是改变a的值，相当于新生成了a。
#可变类型：变量赋值la=[1,2,3,4] 后再赋值la[2]=5则是将list la的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
#python 函数的参数传递：
#不可变类型：类似c++的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#可变类型：类似c++的引用传递，如 列表，字典。如fun（la），则是将la真正的传过去，修改后fun外部的la也会受影响
#python中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
#匿名函数
#python 使用 lambda 来创建匿名函数。
#lambda只是一个表达式，函数体比def简单很多。
#lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

#dir()函数
#dir()函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
#返回的列表容纳了在一个模块里定义的所有模块，变量和函数

#globals()和locals()函数
#根据调用地方的不同，globals()和locals()函数可被用来返回全局和局部命名空间里的名字。
#如果在函数内部调用locals()，返回的是所有能在该函数里访问的命名。
#如果在函数内部调用globals()，返回的是所有在该函数里能访问的全局名字。
#两个函数的返回类型都是字典。所以名字们能用keys()函数摘取。

#reload()函数
#当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
#因此，如果你想重新执行模块里顶层部分的代码，可以用reload()函数。该函数会重新导入之前导入过的模块。

'''
4、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求：1：页面显示 序号 + 商品名称，如：
      	1 手机
	   	2 电脑
     		 …
     2： 用户输入选择的商品序号，然后打印商品名称
  3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。

'''







