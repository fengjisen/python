# 继承 ： 什么是什么的关系
# 单继承 *****
    # 先抽象再继承，几个类之间的相同代码抽象出来，成为父类
    # 子类自己没有的名字，就可以使用父类的方法和属性
    # 如果子类自己有，一定是先用自己的
    # 在类中使用self的时候，一定要看清楚self指向谁
# 多继承 ***
    # 新式类和经典类：
        # 多继承寻找名字的顺序 ： 新式类广度优先，经典类深度优先
        # 新式类中 有一个类名.mro方法，查看广度优先的继承顺序
        # python3中 有一个super方法，根据广度优先的继承顺序查找上一个类


