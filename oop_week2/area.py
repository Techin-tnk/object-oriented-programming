print("โปรเเกรมหาพื้นที่ 3 เหลี่ยม")
base= int(input("ใส่ค่าฐาน"))
heght = int(input("ใส่ค่าสูง"))
a = 0.5 * base * heght
print(f'ค่าของพื้นที่ 3 เหลี่ยม = {a}')

print("โปรเเกรมหาพื้นที่ 4 เหลี่ยมจัตุรัส")
side = int(input("ใส่ค่าด้าน"))
b = side * side
print(f"ค่าพื้นสี่เหลี่ยม = {b}")

print("โปรเเกรมหาพื้นที่ 4 เหลี่ยมผืนผ้า")
wide = int(input("ใส่ค่ากว้าง"))
long = int(input("ใส่ค่ายาว"))
c = wide * long
print(f"ค่าพื้นสี่เหลี่ยมผืนผ้า = {c}")

print("โปรเเกรมหาพื้นที่ วงกลม")
radius = int(input("ใส่รัศมี"))
d = 3.14 * radius **2 
print(f"ค่าพื้นที่วงกลม = {d}")