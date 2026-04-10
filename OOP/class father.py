### 练习 5：继承练习
# 定义父类 `Animal`，子类 `Dog`、`Cat`。
# 要求：
# - 父类有 `name`
# - 父类有 `speak()` 方法
# - 子类重写 `speak()`
# 这个练习重点不是业务，而是理解继承和方法重写。

#父类：动物
class Animal:
    def __init__(self, name, speak):
        self.name = name
        self.speak = speak

#动物的子类：狗
class Dog(Animal):
    def __init__(self, name, speak):
        super().__init__(name, speak)
        self.speak = "汪汪"

#动物的子类：猫
class Cat(Animal):
    def __init__(self, name,speak):
        super().__init__(name, speak)
        self.speak = "喵喵"

dog = Dog("xiaohu",1)
cat = Cat("daimao",2)
print(dog.speak)
print(cat.speak)