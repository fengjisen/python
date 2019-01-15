# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
l = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and i!=k and j!=k):
                s = str(i)+str(j)+str(k)
                l.append(s)
for m in l:
    print(m)
print(len(l))
print('--------------------------')

# 输入某年某月某日，判断这一天是这一年的第几天？
year = input('请输入当前年份:')
mouth = input('请输入当前月份:')
day = input('请输入当前日')
