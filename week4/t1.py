def axb(a,b):
   c = a*b
   print(c)
a= 10
b= 6
axb(b=a,a=b)

def axb(num1,num2):
   sum = num1*num2
   print(sum)
num1 = 10
num2 = 6
axb(num2=num1,num1=num2)

def axb(num1,num2):
   sum = num1*num2
   print(sum)
a = int(input("ใส่ตัวต้น :"))
b = int(input("ใส่ตัวปลาย :"))
axb(a,b)

def axb(num1,num2):
   sum = num1*num2
   return sum 
a = 10
b = 5
c = axb(a,b)
print(c)