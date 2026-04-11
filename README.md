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

 ## 2.文件读写
### 2.1 文件路径基础
1. 当前工作目录 (CWD - Current Working Directory)
   - 运行.py文件时所在文件夹
2. 相对路径
   - 相对于你的 CWD（当前工作目录）来计算的路线，是实际工程中最常用的方式。
   - `.` (一个点)： 代表当前目录（“就在我脚下”）。通常可以省略。
   - `..` (两个点)： 代表上一级目录（“退回上一层”）。
3. 绝对路径
   - 绝对路径永远是从“根目录”（Windows的 C:\ 或 D:\或者 Linux/Mac 的 / ）开始写的。
   - 优点：绝对准确，永远不会找错。
   - 缺点：不可移植！ 如果你把整个 Engine_Sim 文件夹发给你的同事，而他把文件夹放在了 E盘，那你的绝对路径代码在他的电脑上就会直接崩溃。
4. Windows 路径与转义问题
   - 在 Windows 系统里，复制出来的路径通常是用反斜杠 \ 的，比如：`C:\new_project\test.csv`。但在Python 的字符串里，反斜杠 \ 具有转义（Escape）的作用：\n 并不代表两个字母，而是代表“回车换行”；\t 代表“Tab 制表符”。所以，如果你直接把该路径粘进代码就会报错，也找不到对应文件。
   - 怎么避免这个问题？
     - 方式1：在字符串开头加一个 r，告诉 Python里面所有的斜杠都是普通字符，不用转义。`path = r"C:\new_project\test.csv"`
     - 方式2：全部换成正斜杠 /。虽然 Windows 默认用反斜杠，但其实 Windows 底层完全认识正斜杠 /！而且正斜杠在 Linux 和 Mac 上也是通用的。`path = "C:/new_project/test.csv"`
     - 方式3：用双反斜杠 \\，用第一个 \ 去把第二个 \ 转义成普通字符。`path = "C:\\new_project\\test.csv"`

### 2.2 文件基本操作
1. open("文件路径", "模式", encoding = "utf-8")
   - 模式包括：r（读）、w（写）、a（追加）、r+（读写）、a+（追加读写）
   - open文件之后需要file.close()关闭文件释放资源，但通常不用手动调用close()
2. `with open(...) as f`更常用的访问文件方式
   - 用关键字with，open文件下执行完毕后会自动close()，避免程序出bug时close()不执行，代码更安全。
   - f为自定义的文件变量名。

### 2.3 读取方法
1. 文件指针（File Pointer / Cursor）
   - 你可以把“读取文件”想象成“用眼睛看书”。你的视线停留的那个字，就是文件指针。
   - 每次读取，视线（指针）都会往后移动；如果不手动重置它，读过的内容就不会再读第二遍。
2. `read()`：全量读取
   - 原理： 从当前文件指针所在的位置，一口气把后面所有的内容全部读出来。
   - 返回值： 一个巨大的字符串 (String)，包含了所有的换行符 \n。
   - 适用场景： 文件极小（比如几KB的配置文件），你想对整个文本直接使用字符串操作（比如正则替换）。
   - 缺点：如果文件很大（比如10GB），使用 read() 会把电脑内存撑爆！
   - read(size) 其实可以传入数字，比如 read(5) 表示只读前5个字符，但实际开发中较少这样精细切分字符。
    ```python
    with open("engine_log.txt", "r",encoding="utf-8") as file:
        content = file.read()
        print(repr(content))     # 输出: 'Thrust: 120kN\nTemperature: 1500C\nStatus: Normal'
    ```  
3. `readline()`：单行读取
   - 原理： 从当前指针位置开始，一直读到下一个换行符 \n 为止。
   - 返回值： 单行内容的字符串 (String)（结尾通常自带一个 \n）。
   - 适用场景： 你需要在读取过程中进行复杂的条件判断，比如读到某一行包含 "Error" 时就立刻停止。它非常节省内存，因为每次内存里只有一行数据。
   - 缺点： 如果要读完整个文件，需要自己写 while 循环，代码看起来比较啰嗦。
    ```python
    with open("engine_log.txt", "r", encoding="utf-8") as file:
        line1 = file.readline()
        print(repr(line1)) # 输出: 'Thrust: 120kN\n'
        line2 = file.readline()
        print(repr(line2)) # 输出: 'Temperature: 1500C\n'
    ```
4. `readlines()`：按行全量读取
   - 原理： 它其实是 read() 的变种。它也是一口气读完所有内容，但它会自动帮你根据换行符把文本切开。
   - 返回值： 一个列表 (List)，列表里的每一个元素就是文件里的一行字符串。
   - 适用场景： 文件不大，且你明确需要通过“索引”来访问特定行（比如：我想直接拿到第 100 行的数据 lines[99]）。
   - 缺点：和read（）一样，同样面临内存爆炸的风险
    ```python
    with open("engine_log.txt", "r", encoding="utf-8") as file:
        lines_list = file.readlines()
        print(lines_list)  # 输出: ['Thrust: 120kN\n', 'Temperature: 1500C\n', 'Status: Normal']
        print(lines_list[1]) # 轻松获取第二行数据
    ```
5. `for line in file`:迭代读取
   - 这是 Python 官方最强烈推荐、最优雅、也是最专业的文件读取方式！
   - 原理： Python 的文件对象本身就是一个迭代器（Iterator）。在这个循环中，Python 底层会自动像流水线一样，每次只把一行数据提取到内存中，用完就丢弃，去取下一行。
   - 返回值： 每次循环给你一个代表单行内容的字符串 (String)。
   - 适用场景： 99% 的按行处理场景，用这种写法不仅代码最简洁，而且永远不会内存溢出。
    ```python
    with open("engine_log.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())   # 去除每行末尾自带的 \n 并打印
    ```

### 2.4 写入模式
1. 在 Python 写入文件时，**写入模式**（w / a / r+ / a+）决定了你对旧数据的态度，而**写入方法**（write / writelines）决定了你塞进去的数据格式。
2. `w`:覆盖写入模式(Write)
   - 原理： 如果这个文件已经存在，Python 会把它清空，然后再开始写入新内容。如果文件不存在，它会帮你新建一个。
   - 适用场景： 保存最终结果、生成全新的报告、每次都需要重新覆盖的临时配置文件。
3. `a`:追加写入模式(Append)
   - 原理：写入的新内容，会紧接着文件原有内容往后排。如果文件不存在，它也会帮你新建一个。
   - 光标初始位置： 文件的最末尾。
   - 适用场景： 记录运行日志（Log）。
4. `r+`:读写模式
   - 本质： 以“读”为主，赋予“写”的权限。如果文件不存在，直接报错 FileNotFoundError。
   - 光标初始位置： 文件的最开头。
   - 在 r+ 模式下写入，不是插入，而是“逐字覆盖替换”！就像你拿着涂改液在纸上改字，写几个新字，就会盖住原本位置上的几个旧字，后面的内容不会自动往后挪。
   - 适用场景： 非常少用。通常只用于修改固定长度的二进制文件，或者明确知道要覆盖头部几个字符的特殊场景。在普通的文本处理中，我们极少用 r+ 去改文件内容，因为容易把数据搞乱。
    ```python
    # 假设 config.txt 原本的内容是：Thrust: 120kN
    with open("config.txt", "r+") as file:
        file.write("NEW_")     # 1. 光标在最开头，我们写点东西
            # 此时文件内容变成了：NEW_st: 120kN  (开头的 'Thru' 被 'NEW_' 覆盖了！)
        content = file.read()    # 2. 如果我们紧接着读取：
        print(content) # 输出: 'st: 120kN' (因为刚才写完，光标停在下划线后面，只读出了剩下的)
    ```
5. `a+`: 追加读写模式
   - 本质： 以“追加写”为主，赋予“读”的权限。文件如果不存在会自动新建。
   - 光标初始位置： 文件的最末尾。
   - 在 `a+`模式下，关于读：因为一打开文件，光标就在最末尾，如果你直接执行 read()，你会读到一个空字符串！你必须用 file.seek(0) 把光标手动拉回开头才能读到东西。
   - 在 `a+`模式下，关于写：无论你用 seek() 把光标移动到了哪里，只要你一执行 write()，系统会瞬间把光标强制拽回文件最末尾，然后把内容追加进去！你绝对不可能在 a+ 模式下把内容写到文件中间。
   - 适用场景： 非常适合处理日志文件。你随时可以 seek(0) 回头去查阅历史日志，但一旦要写入新日志，它保证绝对只会追加在最后，绝不会破坏前面的历史记录。
    ```python
    # 假设 log.txt 原本内容是：Start
    with open("log.txt", "a+") as file:
        # 1. 尝试直接读：什么都读不到，因为光标在最后
        print("直接读:", repr(file.read()))       # 输出: ''
        
        # 2. 把光标移到开头，再读
        file.seek(0)
        print("移到开头后读:", repr(file.read()))        # 输出: 'Start'
        
        # 3. 此时光标又跑到末尾了。我们尝试把光标移回开头，试图强行在开头写入
        file.seek(0)
        file.write("_End") 
        # 结果：文件内容变成了 'Start_End'。
        # 尽管你 seek(0) 了，write 操作依然强制在末尾追加！
    ```

### 2.5 写入方法
1. `write(string)`：单次写入（最常用）
   - 接收参数： 必须是一个字符串 (String)。
   - 适用场景： 几乎 90% 的写入场景。如果你要把数字存进去，必须先用 str() 转换成字符串。
2. `writelines(list)`：单次写入（最常用）
   - 接收参数： 一个列表 (List)（或其他可迭代对象），列表里的每一个元素都必须是字符串。
   - 适用场景： 当你在内存里已经处理好了一个包含很多行数据的列表，想一次性把它们全部“倒”进文件里。
   - 注意：writelines 绝对不会自动帮你加换行符！ 如果你的列表元素里没有 \n，它会把所有元素死死地拼成一长串！
  
### 2.6 JSON 文件处理
1. JSON文件是什么？
   - JSON (JavaScript Object Notation)文件，本质是一个普通的文本文件（与txt一样），里面装着按 JSON 规则排版好的英文字符，专门用来在不同的系统或编程语言之间传输和存储数据。
   - JSON文件三大核心特征：
     - 只有键值对和列表
     - 所有的键必须带双引号
     - 只认识最基础的类型：字符串（双引号）、数字、布尔值（true / false，注意全小写）、空值（null）以及前面说的对象和数组
2. Python 字典 / 列表 与 JSON 的对应关系
   - 只有以下数据类型能被直接转成JSON，记住这张对照表：
     - `dict (字典)`Python —— `object (对象)`JSON —— 一模一样，都是 {}
     - `list, tuple (列表, 元组)`Python —— `array (数组)`JSON —— 元组 () 在变 JSON 时会被强制变成列表 []
     - `str (字符串)`Python —— `string (字符串)`JSON —— JSON 强制要求只能用双引号 ，不能用单引号！
     - `int, float (整数, 浮点数)`Python —— `number (数字)`JSON —— 一模一样
     - `True / False（布尔值）`Python —— `true / false`JSON —— JSON 里的首字母是小写的！
     - `None（空值）`Python —— `null`JSON —— 拼写完全不同
3. `json.dump()`
   - 把 Python 数据打包，写入JSON文件。
   - 使用该方法前必须要先导入内置的 json 模块：`import json`
    ```python
    import json
    
    engine_config = {
        'model': 'WS-15',
        'max_thrust': 150.5,
        'is_active': True,
        'errors': None,
        'components': ('Fan', 'Compressor', 'Turbine')
    }
    
    # 必须加上 encoding='utf-8'，否则遇到中文会乱码！
    with open("config.json", "w", encoding="utf-8") as file:
        json.dump(engine_config, file, indent=4)
        # indent=4 是极其重要的参数！它会让原本挤成一坨的代码，漂亮地缩进换行，方便人类阅读。
    
    print("配置文件已成功保存为 config.json！")
    ```
4. `json.load()`
   - 读取 JSON 文件，拆包成 Python 数据。
   - 使用该方法前必须要先导入内置的 json 模块：`import json`
    ```python
    import json
    
    with open("config.json", "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    
    print(type(loaded_data)) # 输出: <class 'dict'>
    ```
5. `json.dumps()`和`json.loads()`
   -  s 代表 String（字符串）。它们完全不碰硬盘， 纯粹是在内存里完成“Python 数据”和“JSON 字符串”之间的相互转换
   -  `json.dumps()`：将Python的字典打包成JSON格式的字符串
       - 核心适用场景：网络传输。当你的 Python 程序要给前端网页、手机 App 或者外部服务器发送数据时，网线里是传不了 Python 字典的，只能传文本流。所以你必须先用 dumps() 把字典变成字符串，然后再发出去。
        ```python
        import json
        sensor_data = {
            "device_id": "Engine-01",
            "status": "运行中",
            "rpm": 12000
        }
    
        json_string = json.dumps(sensor_data, ensure_ascii=False)
        # 如果不加ensure_ascii=False，你的中文会变成鬼画符一样的 "\u8fd0\u884c\u4e2d"！
        
        print("转换后的数据类型:", type(json_string)) 
        print("准备发送的文本:", json_string)
        ```
  - `json.loads()`：将JSON格式的文本字符串，转成Python 可以操作的字典或列表
      - 核心适用场景：接收网络数据。当你调用别人的 API（比如获取天气、请求 ChatGPT 的回答），别人服务器返回给你的，永远是一段很长的纯文本字符串。你没法直接用 data['temp'] 去拿温度，必须先用 loads() 把它转换回字典。
        ```python
        import json
        api_response_str = '{"city": "Beijing", "weather": "Sunny", "temp": 25.5}'
        print("刚收到的数据类型:", type(api_response_str)) 
        
        parsed_dict = json.loads(api_response_str)
        print("解析后的数据类型:", type(parsed_dict)) 
        print(f"今天 {parsed_dict['city']} 的温度是 {parsed_dict['temp']} 度。")
        ```

### 2.7 CSV 文件处理
1. CSV文件是什么？
   - CSV（Comma-Separated Values）文件，本质是一个普通的文本文件（与txt一样），文本内容为用逗号分割的EXCEL表格数据文本版。
2. `csv.reader（）`：一行行从表格里提取数据 (读取)
   - 需要先import csv
   - 原理： 逐行读取 CSV 文件，自动识别逗号分隔符和双引号，把每一行变成一个 Python 列表 (List)。
   - csv.reader 读出来的所有数据，全部都是字符串 (String)！ 哪怕表格里写的是 1500，读出来也是 "1500"。
   - 都进来的可以用next（）跳过表头
   - 适用场景： 读取历史实验数据、导入配置文件、处理超大表格集（因为它是一行行读的，极其省内存）。
    ```python
    import csv
    
    # 1. 打开刚才写入的 CSV 文件
    with open("engine_tests.csv", "r", encoding="utf-8") as file:
        # 2. 创建 reader 对象
        reader = csv.reader(file)
        
        # 💡 极客小技巧：跳过表头！
        # 因为表格第一行通常是 ["引擎型号", "测试状态", ...], 我们不想把它当成数据处理
        # next() 可以让读取器先走一步，把表头“吃”掉
        header = next(reader)
        print(f"提取到的表头: {header}\n")
        
        # 3. 用 for 循环，一行一行遍历剩下的真实数据
        for row in reader:
            # 此时的 row 是一个列表：['WS-15', '正常', '1500']
            model = row[0]
            status = row[1]
            
            # 记得把字符串转成整数！
            temp = int(row[2]) 
            
            # 做点逻辑判断
            if temp >= 1400:
                print(f"🔥 警告：[{model}] 温度高达 {temp} 度！状态：{status}")
            else:
                print(f"✅ 正常：[{model}] 温度 {temp} 度。")
    ```
3. `csv.writer（）`：一行行把数据装进表格 (写入)
   - 需要先import csv
   - 原理： 接收 Python 的列表 (List)，自动帮你加上逗号，遇到特殊的文本（比如文本里本身就有逗号的）会自动加双引号保护起来，最后写入文件。
   - 在 Windows 系统下，用 open() 写 CSV 时，必须加上 newline='' 参数！ 否则你写出来的表格，每两行之间都会隔着一个恶心的空行！
   - 核心方法：
     - `writerow(list)`：写入单行。
     - `writerows(list_of_lists)`：一次性写入多行。
   - 适用场景： 将程序跑出来的计算结果、爬虫抓取的数据导出成 Excel 能直接打开的表格。
    ```python
    import csv
    
    # 准备我们的测试数据 (注意第二条状态里自带了一个逗号)
    header = ["引擎型号", "测试状态", "最高温度(C)"]
    data_rows = [
        ["WS-15", "正常", 1500],
        ["AL-31", "警告, 振动异常", 1450], # 这里的逗号是陷阱！
        ["C919-Engine", "优秀", 1320]
    ]
    
    # 1. 打开文件准备写入 (千万别忘了 newline='')
    with open("engine_tests.csv", "w", newline="", encoding="utf-8") as file:
        # 2. 创建 writer 对象 (告诉 Python：这是一个 CSV 写入器)
        writer = csv.writer(file)
        
        # 3. 写入表头 (单行)
        writer.writerow(header)
        
        # 4. 批量写入数据 (多行)
        writer.writerows(data_rows)
    
    print("✅ CSV 表格导出成功！")
    ```

### 2.8 文件是否存在
1. `os.path.exists()`：老旧方法
   - import os
   - 用法： 丢给它一个字符串格式的路径，它返回 True（存在）或 False（不存在）。
    ```python
    import os
    
    # 1. 路径本质上只是个字符串
    log_path = "D:/Engine_Sim/logs/ws15_test.csv"
    
    # 2. 判断是否存在
    if os.path.exists(log_path):
        print("✅ 找到日志文件！")
    else:
        print("❌ 没找到。")
    ```
2. `pathlib.Path`：越来越常用的新版写法
   - from pathlib import Path
   - 用法： 把字符串用 Path() 包装成一个对象。一旦变成对象，它就拥有了各种超能力。
    ```python
    from pathlib import Path
    base_dir = Path("D:/Engine_Sim/logs")
    
    # 直接用 / 拼接字符串或对象！完全不用管斜杠写反的问题！
    log_file = base_dir / "2026" / "ws15_test.csv" 
    
    if log_file.exists():
        print("✅ 文件存在！")

    print(log_file.name)    # 输出: ws15_test.csv (带后缀的文件名)
    print(log_file.stem)    # 输出: ws15_test (不带后缀的文件名，以前用 os 提取这个极其麻烦！)
    print(log_file.suffix)  # 输出: .csv (后缀名)
    print(log_file.parent)  # 输出: D:\Engine_Sim\logs\2026 (父目录，相当于退上一级)
    
    # 判断它是文件还是文件夹？
    print(log_file.is_file()) # 输出: True 
    print(log_file.is_dir())  # 输出: False
    ```
