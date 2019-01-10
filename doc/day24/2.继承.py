# class A(object):pass   # 父类，基类，超类
# class B:pass   # 父类，基类，超类
# class A_son(A,B):pass # 子类，派生类
# class AB_son(A):pass # 子类，派生类
# 一个类 可以被多个类继承
# 一个类 可以继承多个父类  —— python里
# print(A_son.__bases__)
# print(AB_son.__bases__)
# print(A.__bases__)  # python3 -新式类# 没有继承父类默认继承object
class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.func()
    def func(self):
        print(123)
#
class Dog(Animal):
    def func(self):
        print(456)
    def bite(self,person):
        person.hp -= self.aggr
d = Dog()

# class Person(Animal):
#     pass
#
# jin = Dog('金老板',200,500)
# print(jin.name)

# 狗类 吃 喝 看门(guard)
# 鸟类 吃 喝 下蛋(lay)
# class Animal:
#     def __init__(self):
#         print('执行Animal.__init__')
#         self.func()
#     def eat(self):
#         print('%s eating'%self.name)
#     def drink(self):
#         print('%s drinking'%self.name)
#     def func(self):
#         print('Animal.func')
#
# class Dog(Animal):
#     def guard(self):
#         print('guarding')
#     def func(self):
#         print('Dog.func')
# dog = Dog()

# class Bird(Animal):
#     def __init__(self,name):
#         self.name = name
#     def lay(self):
#         print('laying')



# dog.drink()
# bird.drink()
# dog.guard()
# bird.lay()
# class Animal:
#     def __init__(self,name,aggr,hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#
#     def eat(self):
#         print('吃药回血')
#         self.hp+=100
#
# class Dog(Animal):
#     def __init__(self,name,aggr,hp,kind):
#         Animal.__init__(self,name,aggr,hp)  #
#         self.kind = kind       # 派生属性
#     def eat(self):
#         Animal.eat(self)   # 如果既想实现新的功能也想使用父类原本的功能，还需要在子类中再调用父类
#         self.teeth = 2
#     def bite(self,person):   # 派生方法
#         person.hp -= self.aggr
#
# jin = Dog('金老板',100,500,'吉娃娃')
# jin.eat()
# print(jin.hp)

# class Person(Animal):
#     def __init__(self,name,aggr,hp,sex):
#         Animal.__init__(self,name,aggr,hp)
#         self.sex = sex       # 派生属性
#         self.money = 0       # 派生属性
#
#     def attack(self,dog):
#         dog.hp -= self.aggr
#
#     def get_weapon(self,weapon):
#         if self.money >= weapon.price:
#             self.money -= weapon.price
#             self.weapon = weapon
#             self.aggr += weapon.aggr
#         else:
#             print("余额不足，请先充值")
# # alex = Person('alex',1,2,None)
# # alex.eat()
# # print(alex.hp)
# #
# # jin.bite(alex)
# # print(alex.hp)
#
#
# 父类中没有的属性 在子类中出现 叫做派生属性
# 父类中没有的方法 在子类中出现 叫做派生方法
# 只要是子类的对象调用，子类中有的名字 一定用子类的，子类中没有才找父类的，如果父类也没有报错
# 如果父类 子类都有 用子类的
    # 如果还想用父类的，单独调用父类的:
    #       父类名.方法名 需要自己传self参数
    #       super().方法名 不需要自己传self
# 正常的代码中 单继承 === 减少了代码的重复
# 继承表达的是一种 子类是父类的关系
class Animal:
    def __init__(self,name,aggr,hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
    def eat(self):
        print('吃药回血')
        self.hp+=100

class Dog(Animal):
    def __init__(self,name,aggr,hp,kind):
        super().__init__(name,aggr,hp)  # 只在新式类中有，python3中所有类都是新式类
        self.kind = kind       # 派生属性
    def eat(self):print('dog eating')

# jin = Dog('金老板',200,500,'teddy')
# print(jin.name)
# jin.eat()
# super(Dog,jin).eat()

#






