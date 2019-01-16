# 现在有一个包含N个元素的元组或者序列,怎么将它里面的值解压出来同时赋值给多个元素
# 任何的序列 (或者是可迭代对象) 可以通过一个简单的赋值语句解压并赋值给多个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。
p = (4,5)
x,y = p
print(x) # 4
print(y) # 5
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name,age,price,date = data
print(date) # (2012, 12, 21)
# 如果变量个数和序列元素的个数不匹配，会产生一个异常
# 实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。包括字符串，文件对象，迭代器和生成器。
s = 'Hello'
a,b,c,d,e = s
print(a) # H
# 有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提供特殊的语法。但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_,m,n,_ = data
print(m) # 50
print(n) # 91.1
# 你必须保证你选用的那些占位变量名在其他地方没被使用到。
# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
# Python 的星号表达式可以用来解决这个问题。
r = ('a','b','c','d')
m,n,*s = r
print(m) # a
print(n) # b
print(*s) # c d
print(type(s)) # <class 'list'> # 解压出的带*的永远都是列表类型 不管有多少个  包括0个
q,w,e,r,*t = r
print(q) # a
print(w) # b
print(e) # c
print(r) # d
print(*t) #为空 但是还是list类型

# 星号解压可迭代对象 实现递归操作
def recursion(items):
    tail,*recur = items
    return tail+recursion(recur) if recur else tail
items = [1,4,5,3,7,8,213]
s= recursion(items)
print(s)
# 证明可迭代对象
from collections import Iterable

l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
d = {1: 2, 3: 4}
s = {1, 2, 3, 4}

print(isinstance(l, Iterable)) # True
print(isinstance(t, Iterable)) # True
print(isinstance(d, Iterable)) # True
print(isinstance(s, Iterable)) # True

#为什么可迭代对象都可以被for循环遍历 要想可迭代，内部必须有一个__iter__方法。


#队列
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


