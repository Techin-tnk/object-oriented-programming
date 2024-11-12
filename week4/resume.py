a = int(input("จำนวนที่จะป้อน"))
info = {}
for i in range(1,a+1):
    print(f"กรุณากรอกข้อมูลคนที่ {i}")
    info ["name"] = str(input('กรุณากรอกชื่อ : '))
    info ["nickname"] = str(input('กรุณากรอกชื่อเล่น : '))
    info ["stuid"] = str(input('กรุณากรอกรหัสประจำตัวนักศึกษา : '))
    info ["hobby"] = str(input('กรุณากรอกชื่อ : '))
    info ["fcolor"] = str(input('กรุณากรอกชื่อ : '))
    print("ข้อมูลคนที่" +str(i))
    print(info)