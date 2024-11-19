# 有三个人要买小米su7: 张三--20岁--210000元预算、李四--24岁--250000元预算、王五--25岁--1000000元预算，
# 3个人（随机分配）可选的车的颜色有：黑、白、灰、绿
# 选配列表里面有轮毂--30000元、手机支架--2000元、全车雷达--15000元、人工智能--5000元四个选项，（随机分配）
# 三个人随意挑选，su7基本价格为200000元

# 1.构建出三个买车的人的类及其三个对象并打印
# 2.构建出三个人的车的类及其对象并打印
# 3.在紧张的选配后，算出三个人口袋里面的钱是否能够购买全车
# 4.年龄超过21岁的车主并且颜色不选择黑色的车主还剩多少钱，如果有多个返回值，以列表的形式打印

import random

# 定义一个Person类
class Person:
    def __init__(self, name, age, budget):     # self--实例方法
        self.name = name      # 实例属性  姓名
        self.age = age
        self.budget = budget
    def __str__(self):   # 将定义对象转换为字符串
        return f'{self.name}--{self.age}岁--{self.budget}预算'

# 定义一个Car类
class Car:
    def __init__(self, owner, color, options):
        self.owner = owner
        self.color = color
        self.options = options
        self.base_price = 200000
    def total_price(self):
        return self.base_price + sum(option['price'] for option in self.options)
    def __str__(self):
        return f'{self.owner.name}的车的颜色是：{self.color}，选配列表：{self.options}'

# 买车人信息列表
person_data = [
    {'name': '张三', 'age': 20, 'budget': 210000},
    {'name': '李四', 'age': 24, 'budget': 250000},
    {'name': '王五', 'age': 25, 'budget': 1000000},
]

# 选配信息列表
options = [
    {'name': '轮毂', 'price': 30000},
    {'name': '手机支架', 'price': 2000},
    {'name': '全车雷达', 'price': 15000},
    {'name': '人工智能', 'price': 5000}
]

# 车的颜色选项
colors = ['黑', '白', '灰', '绿']

# 1.创建Person对象并打印
#法一：
# persons = []  # 初始化一个空列表来存储 Person 对象
# for data in person_data:
#     person = Person(data['name'], data['age'], data['budget'])  # 创建一个新的Person对象
#     persons.append(person)      # 将新的Person对象添加到persons列表中
#简化：
persons = [Person(data['name'], data['age'], data['budget']) for data in person_data]
for person in persons:
    print(person)

# 2.创建Car对象并打印
#法一：
# cars = []  # 初始化一个空列表来存储 Car 对象
# for person in persons:
#     color = random.choice(colors)     # 随机选择一个颜色
#     options_list = random.sample(options, random.randint(0, len(options)))    # 随机选择一个选配列表
#     car = Car(person, color, options_list)  # 创建一个新的Car对象
#     cars.append(car)  # 将新的Car对象添加到cars列表中
#简化：
cars = [Car(person, random.choice(colors), random.sample(options, random.randint(0, len(options)))) for person in persons]
for car in cars:
    print(car)

# 3.计算三个人是否买得起车
# 法一：
# can_afford = {}    # 初始化一个空字典来存储是否买得起的结果
# for person, car in zip(persons, cars):    # 遍历persons和cars列表;zip函数接受两个或多个可迭代对象作为参数，将它们对应的元素打包成一个元组的列表
#     can_afford[person.name] = person.budget >= car.total_price()    # 计算每个人的预算是否大于等于车的总价，并将结果存储在字典中
# 简化：
can_afford = {person.name: person.budget >= car.total_price() for person, car in zip(persons, cars)}
# 打印每个人是否买得起车
print('三个人是否买得起车：', can_afford)

# 4.计算年龄超过21岁且颜色不是黑色的车主剩余的钱
remaining_budget = []
for person, car in zip(persons, cars):
    if person.age > 21 and car.color != '黑':
        remaining_budget.append(person.budget - car.total_price())
print('年龄超过21岁且颜色不是黑色的车主剩余的钱：', remaining_budget)