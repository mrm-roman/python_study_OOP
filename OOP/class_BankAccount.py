# ### 练习 2：银行账户类
# 定义 `BankAccount` 类，包含：
# - 账户名
# - 余额
# 方法要求：
# - 存款
# - 取款
# - 查询余额
# 扩展要求：
# - 余额不足时报错或提示
# - 不能存负数
# - 打印交易后的余额

# 这个练习特别适合后面和异常处理结合。

class BankAccount:
    def __init__(self, credits, balance):
        self.__credits = credits
        self.__balance = balance

    #存款
    def deposit(self, amount):
        if amount < 0:
            print("You cannot deposit negative amounts")
        else:
            self.__balance += amount

    #取款
    def withdraw(self, amount):
        if amount < 0:
            print("You cannot withdraw negative amounts")
        elif amount > self.__balance:
            print("Not enough money")
        else:
            self.__balance -= amount

    #查询余额
    def check_balance(self):
        return self.__balance

# 测试 1
print("\n【测试 1：常规流程】")
account1 = BankAccount("Roman", 1000)
account1.deposit(500)
account1.withdraw(200)
print(f"您的余额为{account1.check_balance()}")

# 测试 2
print("\n【测试 2：余额不足测试】")
account2 = BankAccount("李四", 500)
account2.withdraw(800)  # 这里应该拦截，且余额不应该变成 -300
print(f"您的余额为{account2.check_balance()}")

# 测试 3
print("\n【测试 3：非法输入测试】")
account3 = BankAccount("王五", 300)
account3.deposit(-50)   # 这里应该拦截非法存款
account3.withdraw(-100) # 这里应该拦截非法取款
print(f"您的余额为{account3.check_balance()}")