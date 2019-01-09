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

#getattr(obj, name[, default]) : 访问对象的属性。
#hasattr(obj,name) : 检查是否存在一个属性。
#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#delattr(obj, name) : 删除属性。
emp1 = employee('aa',16)
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
print(hasattr(emp1,'age'))
getattr(emp1, 'age')    # 返回 'age' 属性的值
print(getattr(emp1,'age'))
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
print(getattr(emp1,'age'))
delattr(emp1, 'age')    # 删除属性 'age'
print(hasattr(emp1,'age'))


#python内置类属性
#__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
#__doc__ :类的文档字符串
#__name__: 类名
#__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
#__bases__ : 类的所有父类构成元素（包含了以个由所有父类组成的元组）
print(employee.__dict__) #{'__module__': '__main__', '__doc__': '所有员工的基类', 'employeecount': 2, '__init__': <function employee.__init__ at 0x0000000001EAB598>, 'displayCount': <function employee.displayCount at 0x0000000001EAB6A8>, 'displayEmployee': <function employee.displayEmployee at 0x0000000001EAB620>, '__dict__': <attribute '__dict__' of 'employee' objects>, '__weakref__': <attribute '__weakref__' of 'employee' objects>}
print(employee.__doc__) # 所有员工的基类
print(employee.__name__) #employee
print(employee.__module__) # __main__
print(employee.__bases__) # (<class 'object'>,)

# python对象销毁(垃圾回收)
# 同Java语言一样，Python使用了引用计数这一简单技术来追踪内存中的对象。
# 在Python内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的引用计数变为0 时， 它被垃圾回收。但是回收不是"立即"的， 由解释器在适当的时机，将垃圾对象占用的内存空间回收。

#python类的继承
#面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
#需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
# 在python中继承中的一些特点：
# 1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
# 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
# 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
# 如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。
# 语法：
# 派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：

# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite
# 你可以使用issubclass()或者isinstance()方法来检测。
# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。



# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods


# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
