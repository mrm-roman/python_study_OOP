# ### 练习 3：图书管理类
# 定义 `Book` 类和 `Library` 类。
# `Book` 包含：
# - 书名
# - 作者
# - 是否借出
# `Library` 包含：
# - 图书列表
# 方法要求：
# - 添加图书
# - 查找图书
# - 借书
# - 还书
# - 显示所有图书

# 这个练习会帮助你理解“一个类里包含另一个类对象”。

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        self.books = []

    #添加图书
    def add_book(self, book_object):
        self.books.append(book_object)
        print(f"成功将《{book_object.title}》加入图书馆！")

    #查找图书
    def find_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                if book.is_borrowed:
                    print(f"《{book_name}》已被借出")
                else:
                    print(f"《{book_name}》可被借阅")
                break
        else:
            print(f"本图书馆没有《{book_name}》这本书")

    #借书
    def borrow_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                if book.is_borrowed == False:
                    print(f"成功借出《{book_name}》，祝您阅读愉快！")
                    book.is_borrowed = True
                elif book.is_borrowed == True:
                    print(f"抱歉，《{book_name}》目前已被借出！")
                break
        else:
            print(f"借书失败：本馆找不到名为《{book_name}》的书籍。")

    #还书
    def return_book(self, book_name):
        flag = False
        for book in self.books:
            if book.title == book_name:
                book.is_borrowed = False
                print(f"《{book_name}》归还成功！")
                flag = True
        if not flag:
            print(f"还书失败：本馆找不到名为《{book_name}》的书籍。")

    #显示所有图书
    def show_all_books(self):
        print("当前馆藏目录：")
        number = 0
        for book in self.books:
            number += 1
            if book.is_borrowed == True:
                print(f"{number}. 《{book.title}》 - {book.author} （状态：已借出）")
            elif book.is_borrowed == False:
                print(f"{number}. 《{book.title}》 - {book.author} （状态：可借阅）")



lib = Library()
book1 = Book("三体", "刘慈欣")
book2 = Book("流畅的Python", "Luciano")
lib.add_book(book1)  # 注意：这里传进去的是 Book 对象，不是字符串！
lib.add_book(book2)

# # 测试 1
# print("\n【测试 1：标准借还流程】")
lib.find_book("三体")
lib.find_book("黑暗森林")
lib.borrow_book("三体")
lib.show_all_books()
lib.return_book("三体")

# 测试 2
print("\n【测试 2：借阅冲突测试】")
lib.borrow_book("流畅的Python")
lib.borrow_book("流畅的Python") # 应该被拦截

# 测试 3
print("\n【测试 3：查无此书测试】")
lib.borrow_book("红楼梦")  # 应该提示找不到
lib.return_book("西游记")  # 应该提示找不到
lib.find_book("红楼梦")