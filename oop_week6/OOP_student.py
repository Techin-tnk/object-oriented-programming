import random

class Student:
    def __init__(self,ชื่อ,นามสกุล,ชื่อเล่น):
        self.name = ชื่อ
        self.lastname = นามสกุล
        self.nickname = ชื่อเล่น
        self.testscore = random.randint(1,10)
    def score(self):
        if self.testscore >= 5:
            print(f"{self.name} {self.lastname} {self.nickname} {self.testscore} สอบผ่าน")
        else:
            print(f"{self.name} {self.lastname} {self.nickname} {self.testscore} สอบไม่ผ่าน")
    
student1=Student (ชื่อ="นายปิติพงค์",นามสกุล="ภูมิพงค์",ชื่อเล่น="ปอน")
student2=Student (ชื่อ="นายชิติพัทธ์",นามสกุล="โสขะรัตน์",ชื่อเล่น="ไนท์") 
student3=Student (ชื่อ="นายกมลศักดิ์",นามสกุล="จิรังพันธ์",ชื่อเล่น="อ็อฟ") 
student4=Student (ชื่อ="นายหนึ่งตะวัน",นามสกุล="เเสงสูงเนิน",ชื่อเล่น="กล้า") 
student5=Student (ชื่อ="นายโยธินันท์",นามสกุล="เเป้นสุข",ชื่อเล่น="ก้อง") 

student1.score()
student2.score()
student3.score()
student4.score()
student5.score()