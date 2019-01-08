'''
比较运算符优先级高于逻辑运算符
and or not
优先级：() > not > and > or
or  x or y  如果x为True则返回x，如果x为False返回y值。因为如果x为True那么or运算就不需要在运算了，因为一个为真则为真，所以返回x的值。
            如果x的值为假，那么or运算的结果取决于y，所以返回y的值
and x and y 如果x为True则返回y值。如果x为False则返回x值。如果x的值为True，and的运算不会结束，会继续看y的值，所以此时真与假取决于y的值，所以x如果为真，则返回y的值。
            如果x为假，那么and运算就会结束运算过程了，因为有一个为假则and为假，所以返回x的值
not not true = false

'''
print(2 > 1 and 1 < 4) # true
print(1 < 4 and 2 > 1) # true
print(1 and 2) # 2
print(0 and 2) # 0
print(-1 and 2) # 2
print(1 > 1 or 3 < 4 or 4 < 5 and 2 > 1 and 9 > 8 or 7 < 6 ) # true
print(not 2 > 1 and 3 < 4 or 4 < 5 and 2 > 1 and 9 > 8  or 7 < 6 ) # true
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8  and  4 > 6 or 3 < 2) # false

print(8 or 3 and 4 or 2 and 0 or 9 and 7) # 8
print(0 or 2 and 3 and 4 or 6 and 0 or 3) # 4
print(5 and 9 or 10 and 2 or 3 and 5 or 4 or 5) # 9


print(6 or 2 > 1) # 6
print(3 or 2 > 1) # 3
print(0 or 5 > 4) # true
# python 变量命名规范
# python数据类型
# int 用于计算
int
i = 1
print(i.bit_length())# 2进制最小位数
#type()判断类型
# bool 用于判断
bool
# str  字符串 存储少量数据用于操作
str
s= 'ABCDEFG'
print(s[0])
print(s[0:4])
print(s[-1])#字符串最后一位就叫-1
print(s[-2])
print(s.index('A'))
# print(s.index('a'))
print()
#为了快速学习 api以后慢慢深入了解

# list 列表 [1,2,3,'a',[1,2]] 储存大量的数据
# 元组(1,2,3,'a',(1,2)) 又叫只读列表
# 字典 dict {"a":"a"} 键值对 相当于java中的map {"a":[],"b":[]}
# 集合 {1,2,3,4,'a'}
# 平常积累些常用的api
