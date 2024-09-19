#1.继承
#就是让类和类之间转变为父子关系，子类默认继承父类的属性和方法
#1.1语法
#class 类名(父类名):
#   代码块
#1.2单继承
# class Person:
#     def eat(self):
#         print('eating')
#     def sleep(self):
#         print('sleeping')
# class Girl(Person):  #Person的子类
#     pass  #占位符，也可以写None，代码里面类下面不写任何东西，会自动跳过，不会报错
# class Boy(Person):
#     pass
# girl = Girl()
# girl.eat()
# girl.sleep()
# boy = Boy()
# boy.eat()
# boy.sleep()
#总结：子类可以继承父类的属性和方法，就算子类自己没有，也可以使用父类的
# from study.function_nl import course1


#1.3继承的传递（多重继承）
#A/B/C C(子类)继承于B(父类),B(子类)继承于A(父类)，C类具有A/B类的属性和方法
#子类拥有父类的父类的属性和方法
# class Father:  #父类
#     def sleep(self):
#         print('睡觉')
#     def eat(self):
#         print('吃饭')
# class Son(Father):  #Father的子类
#     pass
# # son = Son()
# # son.sleep()
# # son.eat()
# class Grandson(Son): #Son的子类
#     pass
# grandson = Grandson()
# grandson.sleep()
# grandson.eat()
#继承的传递性就是子类拥有父类以及父类的父类中的属性和方法


#1.4重写指在子类中定义与父类相同名称的方法
#1.4.1覆盖父类方法
# class Person():
#     def money(self):
#         print('100w要继承')
# class Man(Person):
#     def money(self):
#         #pass
#         print('自己赚1000W')
# man = Man()
# man.money()
#1.4.2对父类方法进行扩展：继承父类的方法，子类也可以增加自己的功能
#1.父亲名.方法名(self)
#2.super().方法名()  --推荐使用
#3.super(子类名,self).方法名()
#super在python里面是一个特殊的类，super()是使用super类创建出来的对象，可以调用父类中的方法
# class Person():
#     def money(self):
#         print('100w要继承')
#     def sleep(self):
#         print('我要睡觉')
# class Man(Person):
#     def money(self):
#         #pass
#         # Person.money(self)
#         # super().money()
#         # super().sleep()  #可以调用父类中的其他方法
#         super(Man,self).money()
#         print('自己赚1000W')
# man = Man()
# man.money()

#2.新式类写法
#2.1class A:  #经典类：不由任意内置类型派生出的类
    #pass
# class Animal:
#     def walk(self):
#         print('我会走路了')
# class Dog(Animal):
#     name = '小狗'
#     def bite(self):  #Dog类是派生类
#         print('我想咬人')
#     #pass  #不是派生类
#2.2 class A()
#2.3 class A(object)  新式类：继承了object类或者该类的子类都是新式类  --推荐使用
#object--对象，python为所有对象提供的基类（顶级父类），提供了一些内置的属性和方法，可以使用dir()查看
#print(dir(object))
#python3中如果一个类没有继承任何类，则默认基础object类，因此python3都是新式类



#3.多继承
#3.1子类可以拥有多个父类，并且具有所有父类的属性和方法
# class Father(object):   #父类一
#     def money(self):
#         print('100W要继承')
# class Mother(object):  #父类二
#     def money2(self):
#         print('又100W要继承')
# class Child(Father, Mother):#子类
#     pass
# child = Child()
# child.money()
# child.money2()

#3.2不同的父类存在同名的方法
#开发时需要尽量避免这种情况发生
# class Father(object):   #父类一
#     def money(self):
#         print('100W要继承')
# class Mother(object):  #父类二
#     def money(self):
#         print('又100W要继承')
# class Child( Mother,Father):#子类
#     pass
# child = Child()
# child.money()
#有多个父类的属性和方法，如果多个父类具有同名方法的时候，调用就近原则，括号内哪个离得最近，优先调用哪个

#3.3方法的搜索顺序（了解）
#python中内置的属性__mro__可以查看方法搜索顺序
# print(Child.__mro__)
#搜索方法时，会先按照__mro__的输出结果，从左往右的顺序查找
#如果在当前类中找到了方法，就直接执行，不再搜索
#如果找到最后一个类，还没有找到这个方法，程序就会报错

#3.4多继承的弊端
#容易引发冲突
#会导致代码的复杂度添加

#4.多态
#指同一种行为具有不同的表现形式
#4.1多态的前提
#继承
#重写
# print(10+10)  #算术运算符：可以实现整形之间的相加操作
# print('10'+'10')  #字符串拼接：实现字符串之间的拼接操作
# class Animal(object):
#     """父类：动物类"""
#     def shout(self):
#         print('动物会叫')
# class Dog(Animal):
#     """"子类一：狗类"""
#     def shout(self):
#         print('小狗汪汪叫')
# class Duck(Animal):
#     """"子类二：鸭类"""
#     def shout(self):
#         print('小鸭嘎嘎嘎')
# dog = Dog()
# dog.shout()
# duck = Duck()
# duck.shout()

#4.2多态性：一种调用方式，不同的执行结果
# class Animal(object):
#     def eat(self):
#         print('eatttttt!')
# class Dog(Animal):
#     def eat(self):
#         print('wangwang')
# class Pig(Animal):
#     def eat(self):
#         print('hengheng')
# #多态性：定义一个统一的接口，一个接口多种实现
# def test(obj):  #obj
#     obj.eat()
# animal  = Animal()
# dog = Dog()
# pig = Pig()
# test(animal)
# test(dog)
# test(pig)
#test函数传入不同的对象，执行不同对象的eat方法


#5.静态方法
#使用@staticmethod来进行修饰,静态方法没有self,cls参数的限制
#静态方法与类无关，可以转换成函数使用
# class Person(object):
#     @staticmethod
#     def study(name):
#         print(f'{name}会学习')
# #静态方法既可以使用对象访问，也可以使用类访问
# Person.study('dingding')
# pe = Person()
# pe.study('dingding') #调用方法时传参
#取消不必要的参数传递，有利于减少不必的内存占用和性能消耗

#6.类方法
#使用装饰器@classmethod来标识为类方法，对于类方法，第一个参数必须是类对象，一般是以cls作为第一个参数
#class 类名：
#   @classmethod
#    def 方法名(cls,形参)
#       方法体
#类方法内部可以访问类属性，或者调用其他的类方法
# class Person(object):
#     @classmethod
#     def study(cls):
#         print('cls:',cls)  #cls代表类对象本身，类本质上就是一个对象
#         print('人类在睡觉')
#         print(cls.name)
# print(Person)
# Person.study()
#当方法中需要使用到类对象(如访问私有类属性等)，定义类方法
#类方法一般是配合类属性使用
#总结
#1.实例方法:方法内部访问实例属性，方法内部可以通过类名,类属性名来访问类属性
#2.静态方法@statIcmethod:方法内部，不需要访问实例属性和类属性，
#如果要访问类屈性，通过类名,类属性名访问，不能访问实例属性
#3.类方法@classmethod:方法内部只需要访问类属性，可以通过cls.类属性名访问类属性，不能访问实例属性
# class Person(object):
#     name = '小丁' #类属性
#     def __init__(self):
#         self.age = 18  #实例属性：对象私有的
#     # def play(self):    #实例方法
#     #     #在实例方法中访问类属性
#     #     print(f'{Person.name}在玩游戏')
#     #     print(self.age)
#     @classmethod  #静态方法：类中的函数，形参没有限制
#     def introduce():
#         # print(f'我是{Person.name}')  #静态方法能够访问到类属性，但是无意义
#         pass
#     @classmethod  #类方法：针对类存在的方法
#     def introduce(cls):  #cls代表类对象本身
#         print(cls.name)
#         # print(self.age)  #报错
# pe = Person()
# pe.play()
# pe.introduce()

#类属性是公共的，所有方法内部都能够访问到，静态方法不需要访问类属性，因为静态方法和类、对象没有关联，
#实例属性是私有的，只有实例方法内部能够访问到
