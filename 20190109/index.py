class employee:
    '所有员工的基类'
    employeecount = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        employee.employeecount += 1
    def displayCount(self):
        print('Total Employee %d' %employee.employeecount)
    def displayEmployee(self):
        print("Name:",self.name,",Age:",self.age)
employee('fjs',23).displayEmployee() # Name: fjs ,Age: 23
employee.displayCount(employee) # Total Employee 1
'''
empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
self代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
'''


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test() # <__main__.Test object at 0x00000000027D35C0>
t.prt() # <class '__main__.Test'>
'''
从执行结果可以很明显的看出，self代表的是类的实例，代表当前对象的地址，而self.class则指向类。
self不是python关键字，我们把他换成w3cschool也是可以正常执行的:
'''


class Test:
    def prt(w3cschool):
        print(w3cschool)
        print(w3cschool.__class__)


t = Test() # <__main__.Test instance at 0x10d066878>
t.prt() # __main__.Test
