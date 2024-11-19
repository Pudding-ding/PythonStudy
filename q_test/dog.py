# 写一个 狗的类，属性有   姓名，品种，价格，体重 ，类方法有  能力（可以打印一行文字就行）
# 随机初始化三只狗，品种啥的自己编
# 按照  价格  对狗进行排序，按照从大到小的顺序，输出每只狗的体重
# 要求：不允许用系统自带的排序方法，自己通过比大小，手写一个排序

import random

# 定义一个Dog类
class Dog:
    def __init__(self, name, breed, price, weight):
        self.name = name
        self.breed = breed
        self.price = price
        self.weight = weight
    def ability(self):
        print(f'{self.name} is a good dog.')
    def __str__(self):
        return f'{self.name} ({self.breed}) - Price: {self.price}元, Weight: {self.weight}kg'

# 随机初始化三只狗
# dogs = ['Dahuang', 'Shier', 'Qiuqiu']
# names = []
# breeds = ['Golden Retriever', 'Akita', 'Labrador']
# for name, breed in zip(names, breeds):
#     price = random.randint(1000, 5000)
#     weight = random.uniform(20.0, 50.0)
#     dogs.append(Dog(name, breed, price, weight))

dogs = [
    Dog('Dahuang', 'Golden Retriever', random.randint(1000, 5000),  round(random.uniform(20.0, 60.0), 2)),
    Dog('Shier', 'Akita', random.randint(1000, 2000), round(random.uniform(20.0, 60.0), 2)),
    Dog('Qiuqiu', 'Labrador', random.randint(1000, 5000), round(random.uniform(20.0, 60.0), 2))
]

# 排序方法
def sort_dogs_by_price(dogs):
    n = len(dogs)
    for i in range(n):
        for j in range(0, n-i-1):
            if dogs[j].price > dogs[j+1].price:
                dogs[j], dogs[j+1] = dogs[j+1], dogs[j]   #如果当前狗的价格大于下一只狗的价格，则交换它们的位置
    return dogs

# 排序并输出体重
sorted_dogs = sort_dogs_by_price(dogs)
for dog in sorted_dogs:
    print(dog)  # 按照价格顺序打印每只狗的详细信息
weights = [f'{dog.weight }kg'for dog in sorted_dogs]
print(weights)