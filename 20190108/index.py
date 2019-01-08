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






