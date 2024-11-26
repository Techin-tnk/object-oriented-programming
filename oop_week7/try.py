while True:
    try:
        print("โปรเเกรมหาพื้นที่สี่เหลี่ยม")
        side = int(input("ใส่ค่าด้าน"))
        b = side * side
        if side == 0:
            raise ZeroDivisionError
        elif side < 0:
            raise Exception
        print(f"ค่าพื้นสี่เหลี่ยม = {b}")

        print("โปรเเกรมหาพื้นที่ 3 เหลี่ยม")
        base = int(input("ใส่ค่าฐาน :"))
        heght = int(input("ใส่ค่าสูง :"))
        if base == 0:
            raise ZeroDivisionError
        elif base <0:
            raise Exception
        a = 0.5 * base * heght
        print(f'ค่าของพื้นที่ 3 เหลี่ยม = {a}')
        
        print("โปรเเกรมหาพื้นที่ วงกลม")
        radius = int(input("ใส่รัศมี :"))
        d = 3.14 * radius **2 
        if radius == 0:
            raise ZeroDivisionError
        elif radius <0:
            raise Exception
        print(f"ค่าพื้นที่วงกลม = {d}")
    except ValueError:
        print("ใส่เฉพาะตัวเลข")
    except ZeroDivisionError:
        print("ห้ามใส 0")
    except:
        print("ห้ามใส่ค่าติดลบ")