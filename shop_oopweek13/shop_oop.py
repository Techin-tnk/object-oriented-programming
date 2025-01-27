class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price 
        self.__stock = stock 

    def update_price(self, amount):
        if amount > 0:
            self.__price = amount
        else:
            print("ราคาสินค้าต้องมากกว่า 0")
        return self.__price

    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
        else:
            print("ไม่สามารถเพิ่มสินค้าได้")

    def discount_stock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
        else:
            print("ไม่สามารถลดสินค้าได้")

    def check_product(self):
        return f"ชื่อสินค้า: {self.name}\nราคาสินค้า: {self.__price} บาท\nจำนวนสินค้า: {self.__stock}"


class Phone(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock) 
        self.brand = brand

    def check_product(self):
        return f"{super().check_product()}\nแบรนด์: {self.brand}"


class Notebook(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand

    def check_product(self):
        return f"{super().check_product()}\nแบรนด์: {self.brand}"

class Clothes(Product):
    def __init__(self, name, price, stock, size, apparel, brand):
        super().__init__(name, price, stock)
        self.size = size
        self.apparel = apparel
        self.brand = brand

    def check_product(self):
        return (f"{super().check_product()}\nขนาด: {self.size}\n"
                f"ประเภทเครื่องแต่งกาย: {self.apparel}\nแบรนด์: {self.brand}")

phone1 = Phone("VIVO Y100", 12000, 100, "VIVO")
notebook1 = Notebook("Lenovo V15 G4 ABP", 14873, 100, "Lenovo")
clothes1 = Clothes(
    "เสื้อยืด New Year Snake Cartoon Graphic Over Fit T-Shirts New York Yankees",
    2390,
    100,
    "XS",
    "T-Shirts",
    "MLB",
)

print(phone1.check_product())
print(notebook1.check_product())
print(clothes1.check_product())
