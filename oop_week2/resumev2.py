name = input("โปรดกรอกชื่อ\n")
age = input("โปรดกรอกอายุ\n")
stuid = input("โปรดกรอกรหัสประจำตัวนักศึกษา\n")
year = input("โปรดกรอกชั้นปี\n")
nickname = input("โปรดกรอกชื่อเล่น\n")
height = float(input("โปรดกรอกส่วนสูง\n"))
weight = float(input("โปรดกรอกน้ำหนัก\n"))
print(f"ชื่อ:  {name}  อายุ:  {age}")
print(f"รหัสประจำตัวนักศึกษา:  {stuid}  ชั้นปี:  {year}")
print(f"ชื่อเล่น:  {nickname}")
print(f"ส่วนสูง:  {height}  น้ำหนัก: {weight}")
print(f"ส่วนสูง + น้ำหนัก = {height + weight}")