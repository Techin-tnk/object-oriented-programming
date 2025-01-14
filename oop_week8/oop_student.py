class Student:
    def __init__(self,ชื่อ,รหัสนักศึกษา,อายุ,เกรด):
        self.name = ชื่อ
        self.id = รหัสนักศึกษา
        self.age = อายุ
        self.grades = เกรด

    def updateScore(self,คณิต,ไทย,อังกฤษ,วิทย์,สังคม):
        self.grades["คณิต"] = คณิต
        self.grades["ไทย"] = ไทย
        self.grades["อังกฤษ"] = อังกฤษ
        self.grades["วิทย์"] = วิทย์
        self.grades["สังคม"] = สังคม

    def scoreToGrade(self):
        for subject, score in self.grades.items():
            if score >= 80:
                self.grades[subject] = 4
            elif score >= 70:
                self.grades[subject] = 3
            elif score >= 60:
                self.grades[subject] = 2
            elif score >= 50:
                self.grades[subject] = 1
            else :
                self.grades[subject] = 0

    def calculateGrade(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def showInformation(self):
        return f"ชื่อ : {self.name} หมายเลขประจำตัว : {self.id} อายุ : {self.age} เกรดเฉลี่ย : {self.calculateGrade()}"
        
        
student1 = Student("ปิติพงศ์","67319010031",19, {})

student1.updateScore(80,45,60,70,80)
print(student1.grades)

student1.scoreToGrade()
print(student1.grades)

print(f"{student1.name} ได้เกรดเฉลี่ย {student1.calculateGrade()}")

print(student1.showInformation())