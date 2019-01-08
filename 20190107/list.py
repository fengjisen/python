s = '21'
s1 = bool(s)
print(s1)

#list
l = [1,'q',2,'w',3,'e',4,'r']
print(l)
l1 = l.remove(1)
print(l)
print(l1)
l2 = l.pop(1)
print(l)
print(l2)



print('='*100)
#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
import random;
offices = [[],[],[]];
names = ['q','w','e','r','a','s','d','f'];
i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for temp in offices:
    print('办公室%d的人数是%d' %(i,len(temp)))
    i+=1
    for name in temp:
        print("%s" % name, end='')
    print("\n")
    print("-" * 20)
#dict
dict