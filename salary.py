class Salary:
    def __init__(self,ชื่อ,อาชีพ,เงินเดือน):
        self.name = ชื่อ
        self.occupation = อาชีพ
        self.salary = เงินเดือน
    def salaryyear(self):  
        return self.salary*12
    
salary1=Salary (ชื่อ="โซเฟีย",อาชีพ="ครู",เงินเดือน=12000)
salary2=Salary (ชื่อ="ปีเตอร์",อาชีพ="หมอ",เงินเดือน=45000)
salary3=Salary (ชื่อ="บ็อบ",อาชีพ="โปรเเกรมเมอร์",เงินเดือน=40000)

print(f"{salary1.name} ประกอบอาชีพ {salary1.occupation} มีเงินเดือนทั้งปี = {salary1.salaryyear()}")
print(f"{salary2.name} ประกอบอาชีพ {salary2.occupation} มีเงินเดือนทั้งปี = {salary2.salaryyear()}")
print(f"{salary3.name} ประกอบอาชีพ {salary3.occupation} มีเงินเดือนทั้งปี = {salary3.salaryyear()}")