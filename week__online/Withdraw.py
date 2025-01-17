class Bank: #คุณสมบัติ
    def __init__(self,id,name,balance): #คุณสมบัติของ Class
        self.id = id
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.__balance -= amount
        else:
            print('ยอดเงินไม่ถูกต้อง')
            def withdraw(self,amount):
                if amount >= 100 and amount <= self.balance:
                    self.__balance -= amount
                else:
                    print('ยอดเงินไม่ถูกต้อง')
                    def showbalance(self):
                        print(self.__balance)
                        return self.__balance
                        
id1 = Bank(1,"sprite",2500) # ผู้ใช้สร้างบช ออฟเจ็คที่ได้จากClass  
id1.balance(200) #ผู้ใช้งาน 
#id1.balance += 500
print(f"คุณ {id1.name} มีเงินคงเหลือ = {id1.balance}")

#Abstaction