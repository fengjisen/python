s='fjsymy'
s1 = s.startswith('fjs')
print(s1)
s2 = s.startswith('fjs',3)
print(s2)
s3 = s.startswith('js',1,3)
print(s3)
s4 = s.find('y')
print(s4,type(s4))
s5 = s.find('a')
s6 = s.find('sy')
print(s5)
print(s6)
s7 =s.index('js')
print(s7)
a = 'f  sdasd js'
a1 = a.__contains__('js')
print(a1)
a.encode('gbk')
a2 = a.rstrip()
print(a2)

b = '   asdas   '
b1 = b.strip() #根据传入的值删除字符串中首尾的字符 前后同时删  直到遇到跟传入字符不同的符号
print(b1)
print(len(b1))


#split
c = 'fjs ymy xk'
c1 = c.split()
print(c1,type(c1))

#format
s  = '我叫{},今年{}，爱好{}'
s1 = s.format('fjs','21','fjs')
print(s1)

#replace
fjs = 'fjs'
fjs1 = fjs.replace('f','a')
print(fjs1)

s = 1
print('this si %s'%s)
while 1:#效率高
    pass

# python中的数据类型
#Number( int float long complex )
#bool
#str
#list 列表  储存大量数据
#tuple 元组  只读列表
#dict 字典 key value
# set 集合

i = 1.1
print(type(i))
q = [1,'2',[1,2]]
print(q)
w = (1,2,3)
print(type(w))
e = {'a':'b'}
print(type(e))
r = {1,'adad',123}
print(type(r))

i= 1
print(type(i))
t = str(i)
print(t,type(t))
y = int(t)
print(y,type(y))

# age1=12
# # age2=age1
# # age3=age2
# # age2=100
# # print(age1,age2,age3);
# # if False:
# #     print("aaa")
# # print("bbb")
# # print("ccc")
'''
count = 1
sum = 0
while count<101:
    sum = sum + count
    count = count+ 1

print(sum)
'''

# count = 1
# while count<101:
#     if count%2==1:
#         print(count)
#     count +=1


# count = 1
# sum = 0
# while count<100:
#     if count%2==1:
#         sum = sum+count
#     else:
#         sum = sum-count
#     count += 1
# print(sum)

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# msg = "name:%s;age:%s" %(name,age)
# print(msg)


# while else 当while被break打断了   就不走else
# count = 0
# while count<=3:
#     count+=1
#     if count == 3:break
#     print(type(count))
#     print("Line",count)
# else:
#     print("1")
# print("2")
# print(0 and 100)
# print( 3 and 4)
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
#
# print(6 or 2>1)
# print(0 or 5<4)
#
# print(5<4 or 3)
# print(0 and 5>4)

# name = input("<<<")
# print(type(name))


# count = 1
# sum = 0
# while count<100:
#     if count == 2:
#         sum = sum - count
#         count += 1
#         continue
#     if count == 88:
#         count += 1
#         pass
#     sum = sum+count
#     count+=1
# print(sum)
s = 'ABCDSOS'
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1
i = s.index('T')
print(i)
