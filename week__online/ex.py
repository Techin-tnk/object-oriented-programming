class Bank: #คุณสมบัติ
    def __init__(self,id,name,balance): #คุณสมบัติของ Class
        self.id = id
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        if amount >= 100:
            self.balance += amount
        else:
            print('ยอดเงินไม่ถูกต้อง')
            def withdraw(self,amount):
                if amount:
                    self.balance -= amount
                else:
                    print('ยอดเงินไม่ถูกต้อง')
                    def showbalance(self):
                        print(self.balance)
                        return self.balance
id1 = Bank(1,"meen",2500) # ออฟเจ็คที่ได้จากClass  
id1.deposit(1000)
print(f"คุณ {id1.name} มีเงิน = {id1.balance}")