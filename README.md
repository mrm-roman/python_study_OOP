# python_study_OOP(2026.4.9~2026.4.）

## 本周学习目录框架:
  1. 面向对象编程（OOP）
  2. 文件读写
  3. 异常处理
  4. 模块、导入与项目结构
  5. Git / GitHub 基础协作流

## 本周总目标：会组织代码、会处理错误、会保存数据、会管理代码版本
- 把一段零散的 Python 代码重构成类
- 能读写 txt / json / csv 文件
- 能用异常处理让程序不轻易崩掉
- 能把代码拆成多个模块文件
- 能独立完成一套 Git 基础操作：初始化、提交、分支、合并
- 做出一个小型命令行项目，并托管到 GitHub

## 学习环境：
- 电脑：Windows11系统 / MacOS系统
- 解释器版本：python 3.12.10
https://www.python.org/downloads/release/python-31210/
- 代码编辑器/IDE：Pycharm2026.1
https://www.jetbrains.com/zh-cn/pycharm/

## 1.面向对象编程（OOP：Object Oriented Programming）
### 1.1面向对象编程 Vs 面向过程编程
- 面向过程编程：（编年体）
  - 教计算机“怎么做”（Step by Step）。
  - 简单直接，适合小项目。
  - 数据、函数是分开独立的
- 面向对象编程：（纪传体）
  - 告诉计算机“用什么人/东西来做”。
  - 适合复杂大项目，但易维护和扩展。
  - 数据和处理数据的方法捆绑。
---
【举个例子】：玩游戏
- 面向过程编程：
  1. 创建角色
  2. 计算攻击力
  3. 扣怪物血量
  4. 判断怪物是否死亡
  5. 发放奖励
- 面向对象编程：（属性就是类里面的变量，行为/方法就是类里面的函数）
  - 对象1：玩家
    - 属性包括：名字、血量、攻击力
    - 行为包括：攻击
  - 对象2：怪物
    - 属性包括：血量、防御力
    - 行为包括：受到攻击、掉落物品
  - 对象3：武器
    - 属性包括：伤害值、形状
    - 行为包括：武器受损
---
### 1.2 类和对象的基本概念
- 类（class）：类是创建对象的模板
- 对象（instance）：对象是类的实例
- 为什么“学生”“商品”“账户”“图书”这种东西适合写成类？
  - 因为它们在现实世界中都是**独立存在的**“名词（实体）”！
  - 判断一个东西适不适合写成类，就看它是不是满足两点：它有特征（属性），它能产生交互（行为）。
  - 【例子】：银行账户（BankAccount）
    - 应该保存的数据（属性）： 户主姓名、账号、当前余额、开户日期、密码。
    - 提供的行为（方法）： 存款（deposit）、取款（withdraw）、查询流水（get_history）、修改密码（change_password）。
    
### 1.3 创建类和实例
1. 创建类：`class NameofClass:`（类的命名通常用首字母大写来区分单词）
  ```python
  class BankAccount:
      # 这是一个特殊的方法（初始化/构造方法），当我们创建新对象时，它会自动运行
      def __init__(self, owner_name, initial_balance):
          # 1. 实例属性：把传进来的数据，永久贴在“我自己”身上
          self.name = owner_name        
          self.balance = initial_balance 
          
      # 2. 实例方法：属于这个对象的行为
      def deposit(self, amount):
          # 动作：修改“我自己”的余额属性
          self.balance = self.balance + amount
          print(f"{self.name} 存入了 {amount} 元。")
  
  # --- 下面是类的使用（实例化） ---
  
  # 创造两个独立的对象
  account_A = BankAccount("Roman", 1000)
  account_B = BankAccount("李四", 500)
  
  # 3. 通过对象调用方法
  account_A.deposit(200)
  ```
2. self的含义？
- 就像你去办理入职，填了一张表。表上有一栏写着**“本人姓名：____”**。这里的“本人”，就是代码里的 self。
  - 张三填表，这里的“本人”指的就是张三。
  - Roman 填表，这里的“本人”指的就是 Roman。
3. 通过对象调用方法：`对象名.方法(参数)`。注：对象命名通常全小写加下划线（如 my_phone）
4. self.name = owner_name：
  - 加上 self.，这个数据就和这个具体的对象终生绑定了
5. 设置默认值
  - 可以给 __init__ 里的参数设置默认值。
  ```python
  class SmartPhone:
      # 我们给 color 设置了默认值 "黑色"，给 5G 设置了默认值 True
      def __init__(self, brand, storage, color="黑色", is_5g=True):
          self.brand = brand
          self.storage = storage
          self.color = color
          self.is_5g = is_5g
  ```

### 1.4 实例方法、类属性、类方法、静态方法
1. 实例属性
  - 每个对象自己的属性，必须为 self.xxx
  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name  #实例属性
          self.age = age
  ```
2. 实例方法
  - 第一个参数必须是self，通过对象调用。
  ```python
  class Student:
      def __init__(self, name, age):
          self.name = name
          self.age = age
      def introduce(self)    #实例方法
          print(f"我叫{self.name}，今年{self.age}岁。)
  ```
3. 类属性
   - 该类下所有对象共享的属性
   - 修改类属性会影响所有实例
  ```python
  class Student:
      school = "BUAA"   #类属性
  ```
4. 类方法
  - 用来修改类属性
  - 方法定义上方加一行@classmethod
  - 方法第一个参数是cls
  ```python
  class Student:
      school = "BUAA"   #类属性

      @classmethod
      def change_school(cls, new_school):     #类方法
        cls.school = new_school
  
  Student.change_school("北京大学")   #调用类方法：类的名称.类方法()
  print(Student.school)
  ```
5. 静态方法
  - 普通函数，只是放在类里，不用self/cls也行
  - 方法定义上方加一行@staticmethod
 ```python
  class Student:
      @staticmethod
      def add(a,b):     #静态方法
        return a+b

  print(Student.add(3,5))    #调用静态方法
  ```

### 1.5 封装
1. 什么是封装？
  - 隐藏内部数据`__变量名`
    ```python
    class BankAccount:
      def __init__(self, balance):
        self.__balance = balance    #私有属性
    ```
  - 通过**方法**控制访问
  - 保护数据+控制逻辑
2. Python 的“伪私有”机制
    - Python 没有真正的强制私有，但它有一套全行业公认的命名潜规则：
      - 单下划线 _name：如果你在属性前加一个下划线，比如 self._temperature。外部依然可以直接访问和修改它。这仅仅是一个警告标识。
      - 双下划线 __name：如果你加两个下划线，比如 self.__core_password。这时你在外部写 engine.__core_password，程序会报错，说找不到这个属性。但其实是Python偷偷把这个变量的名字改成了 _AeroEngine__core_password。如果你非要头铁，写成 engine._AeroEngine__core_password = "123"，你依然能强行改掉它。这是为了防止误用。

### 1.6 继承与多态入门
1. 继承是什么？
   - 子类可以继承父类的属性和方法。如Dog继承了父类Animal的eat（）
    ```python
    class Animal:
        def eat(self):
            print("在吃东西")
  
    class Dog(Animal):   # 继承
        def bark(self):
            print("汪汪叫")

    dog = Dog()
    dog.eat()
    dog.bark()
    ```
    - 如果没有继承，则所有类都要重复写方法。有继承可实现代码复用，写一次就够。
2. 继承的方法重写
   - 如果子类对父类的某个方法不满意，子类可以写一个同名的方法，直接覆盖（重写）掉父类的方法。
3. super()
   - 当子类要复用父类的方法时，就用 `super().父类方法名()` 把父类拉出来干活。
    ```python
    lass Animal:
        def __init__(self, name):
            self.name = name
    
    class Dog(Animal):
        def __init__(self, name, age):
            super().__init__(name)      # 调父类的初始化逻辑
            self.age = age
    ```
4. 多态是什么？
   - 不同对象，对同一个方法有不同反应。如同样是.spark，但不同的对象对应不同的结果，这就是多态。
    ```python
    class Animal:
        def speak(self):
            print("动物在叫")
    
    class Dog(Animal):
        def speak(self):
            print("汪汪")
    
    class Cat(Animal):
        def speak(self):
            print("喵喵")

    animals = [Dog(), Cat()]
    for a in animals:
      a.speak()                 #输出：汪汪  喵喵
    ```
---
**【总结】 面向对象三大核心——封装、继承、多态**
- 封装：保护数据安全，不让你乱改
- 继承：代码复用，少写重复代码
- 多态：灵活扩展，同样的方法在不同的对象身上有不同的表现。
---

### 1.7 特殊方法（了解即可）
  - `__str__`：给人看的，用于定义print(对象)时显示什么，必须return字符串
  - `__repr__`：给程序员/调试看的，用于定义直接输出对象时显示什么 ，必须return字符串
  - 优先级：
    - print()，优先用__str__
    - 如果没有__str__就会用__repr__
    - 直接输入对象用__repr__
    ```python
    class Student:
        def __init__(self, name):
            self.name = name
    
        def __str__(self):
            return f"【str】学生：{self.name}"
    
        def __repr__(self):
            return f"【repr】Student('{self.name}')"
    ```  
 
