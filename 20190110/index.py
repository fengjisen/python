#set 集合  无序 元素不可重复 可变数据类型 但是里面的元素却要是不可变类型
# 不可变类型 hashable type 不可变是可哈希的
from test_moudle import addli
c = addli(1,2)
print(c)

li = [1,1,2,3,4,5,6,6]
s = set(li)
print(s)  #去重 {1, 2, 3, 4, 5, 6}

s = frozenset('fenngjisen')
print(s,type(s)) # frozenset({'f', 'n', 'i', 'e', 'g', 'j', 's'}) <class 'frozenset'>
# fronzenset 冻住的集合 不可变数据类型 无序集合  怎么测试有序 无序  直接for循环打印  每次的结果都是一样的则是有序的
tu1 = (1)
tu2 = (1,)
print(tu1,type(tu1))  # 1 <class 'int'> #元组里面只有一个元素 且不加逗号  这个元素是什么类型 则该元组是什么类型  字典也是一样的
print(tu2,type(tu2)) # (1,) <class 'tuple'>

dic1 = {1:1}
dic2 = {2:2,}
print(dic1,type(dic1)) #{1: 1} <class 'dict'>　
print(dic2,type(dic2))　#　{2: 2} <class 'dict'>
#