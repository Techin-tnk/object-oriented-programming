g = int(input("กรอกคะเเนน"))
if g < 0 or g > 100:
        print("ไม่สามารถกรอกค่านี้ได้")
else:
    if g >= 80:
        print("คุณได้เกรด 4")
    elif g >= 70:
         print("คุณได้เกรด 3")
    elif g >= 60:
         print("คุณได้เกรด 2")
    elif g >= 50:
         print("คุณได้เกรด 1")
    else:
        print("คุณได้เกรด 0")    
        print('ต้องการสอบเเก้หรือ ถ้าต้องการพิมพ์ 1 ไม่ต้องการพิมพ์ 2')
        c = int(input('เลือก :'))
        if c == 1:
            print('สอบผ่านเเล้ว')
        elif c ==2:
            print("สอบตกเหมือนเดิม")
        else:
            print('กรุณาเลือกเเค่ 1 กับ 2')