import keyword
print(keyword.kwlist)
a = [1, 2]
b = a
print(b) # [1, 2]

a.append(3)
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]


# 读取一个文件，显示除了以井号(#)开头的行以外的所有行
f = open('a','r',encoding='utf-8')
l = f.readlines()
for i in l:
    if(i.startswith('#')):
        print('---')
    else:print(i)


# Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
# 它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

#coding=utf-8
class base(object):
    def test(self):
        print('----base test----')
class A(base):
    def test(self):
        print('----A test----')

# 定义一个父类
class B(base):
    def test(self):
        print('----B test----')

# 定义一个子类，继承自A、B
class C(A,B):
    pass


obj_C = C()
obj_C.test()

print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序


