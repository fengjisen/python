# 打开文件 得到文件句柄并赋值给一个变量
f= open('a.txt','r',encoding='utf-8')

#通过句柄对文件操作
data = f.read()

print(data)
# close file
f.close()
'''
打开一个文件包含两部分资源：操作系统级打开的文件+应用程序的变量。在操作完毕一个文件时，必须把与该文件的这两部分资源一个不落地回收，回收方法为：
1、f.close() #回收操作系统级打开的文件
2、del f #回收应用程序级的变量

其中del f一定要发生在f.close()之后，否则就会导致操作系统打开的文件还没有关闭，白白占用资源，
而python自动的垃圾回收机制决定了我们无需考虑del f，这就要求我们，在操作完毕文件后，一定要记住f.close()

虽然我这么说，但是很多同学还是会很不要脸地忘记f.close(),对于这些不长脑子的同学，我们推荐傻瓜式操作方式：使用with关键字来帮我们管理上下文
with open('a.txt','w') as f:
    pass
 
with open('a.txt','r') as read_f,open('b.txt','w') as write_f:
    data=read_f.read()
    write_f.write(data)

注意
'''
with open('a.txt','r',encoding='utf-8') as  read_f,open('b.txt','w',encoding='utf-8') as write_f:
    data = read_f.read()
    write_f.write(data)
# with会自动关闭这些流操作