# ### 练习 4：电商商品与购物车
# 定义：
# - `Product`
# - `Cart`
# 功能要求：
# - 添加商品到购物车
# - 计算总价
# - 删除商品
# - 显示购物车内容
# 扩展要求：
# - 商品有库存
# - 数量不能超过库存

#类：商品库
class Product:
    def __init__(self, name, price, stock, quantity = 0):
        self.name = name
        self.price = price
        self.stock = stock
        self.quantity = quantity


#类：购物车
class Cart:
    def __init__(self):
        self.products = []

    # 添加商品
    def add_product(self, product, quantity):
        if 0 < quantity <= product.stock:
            self.products.append(product)
            product.quantity = quantity
            print(f"✅ [已添加] {product.name} x {quantity} 进入购物车。")
        else:
            print(f"❌ [添加失败] {product.name} 库存不足！剩余库存: {product.stock}，您请求数量: {quantity}。")

    # 显示购物车内容
    def show_items(self):
        print("🛒 [当前购物车]：")
        for item in self.products:
            print(f"- {item.name} | 单价: {item.price} | 数量: {item.quantity}")

    # 计算总价
    def get_total_price(self):
        total_price = 0
        for item in self.products:
            total_price += float(item.price) * float(item.quantity)
        return total_price

    # 删除商品
    def remove_product(self, product_name, delete_quantity):
        for item in self.products:
            if product_name == item.name:
                if 0 < float(delete_quantity) < item.quantity:
                    item.quantity = item.quantity - delete_quantity
                    print(f"{product_name}已删除{delete_quantity}件。")
                elif float(delete_quantity) == item.quantity:
                    self.products.remove(item)
                    print(f"{product_name}已从购物车清空。")
                else:
                    print("非法输入")
                break
        else:
            print(f"购物车中没有{product_name}这项商品，无法删除！")

p1 = Product("iPhone 15", 6000, 5)
p2 = Product("华为 Mate 60", 5500, 2)
cart = Cart()

# # 测试 1
print("\n【测试 1：标准购物流】")
cart.add_product(p1, 1)
cart.add_product(p2, 1)
cart.show_items()
print(f"总计: {cart.get_total_price()} 元")

# 测试 2
print("\n【测试 2：库存拦截测试】")
cart.add_product(p2, 3) # 应该提示库存不足
cart.show_items()

# 测试 3
print("\n【测试 3：移除商品测试】")
cart.remove_product("iPhone 15", 1)
cart.show_items()
print(f"更新后总计: {cart.get_total_price()} 元")