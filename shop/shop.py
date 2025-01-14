class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock
    def updatePrice(self, amount):
        self.__price = amount
        return self.__price
    def addStock(self, amount):
        if amount > 0:
            self.__stock += amount
        else:
            print("ไม่สามารถเพิ่มสินค้าได้")
    def discountStock(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock -= amount
        else:
            print("ไม่สามารถลดสินค้าได้")
    def checkProduct(self):
        return f"ชื่อ : {self.name}\nราคาสินค้า : {self.__price} บาท \nจำนวนสินค้า : {self.__stock}"
    
class Phone(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand
    def checkProduct(self):
        return f"{super().checkProduct()} \nแบรนด์ {self.brand}"
    
class Notebook(Product):
    def __init__(self, name, price, stock, brand):
        super().__init__(name, price, stock)
        self.brand = brand
    def checkProduct(self):
        return f"{super().checkProduct()} \nแบรนด์ {self.brand}"
    
class Clothes(Product):
    def __init__(self, name, price, stock, size, apparel, brand):
        super().__init__(name, price, stock)
        self.size = size
        self.apparel = apparel
        self.brand = brand
    def checkProduct(self):
        return f"{super().checkProduct()} \nขนาด : {self.size} \nเครื่องแต่งกาย : {self.apparel} \nแบรนด์ : {self.brand}"
        
phone1 = Phone("VIVO Y100", 12000, 100, "VIVO")
notebook1 = Notebook("Lenovo V15 G4 ABP", 14873, 100, "Lenovo")
clothes1 = Clothes("เสื้อยืด New Year Snake Cartoon Graphic Over Fit T-Shirts New York Yankees", 2390, 100, "XS", "T-Shirts", "MLB")
print(clothes1.checkProduct())