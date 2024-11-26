sum = 0
while True:  
        num = int(input("ใส่ค่า :"))
        if num != 0:
            sum += num
            print(f"ผลรวมตอนนี้ {sum}")
        else:
            print(f"ผลรวมตอนนี้ {sum}")
            print(f"ผลรวมทั้งหมด {sum}")

        if num == "หยุด":
            break
try:
        if num == 0:
            raise ZeroDivisionError
        elif num < 0:
            raise Exception
 
except ValueError:
        print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
        print("ห้ามใส 0")
except:
        print("ห้ามใส่ค่าติดลบ")