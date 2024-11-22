a = int(input("ป้อนตัวเลข"))
num = []
for i in range(a):
    b = int(input('ค่า : '))
    num.append(b)
c = (sum(num)) // len(num)
print(c)