print("************************************************************")
print("Bai 1")
print("Nhap vao ban kinh hinh tron: ")
a = input()
import math
b = math.pi
a = float(a)
S = b * a*a
print("Dien tich hinh tron voi ban kinh %s la: %s" %(int(a), S))
print("************************************************************")
print("------------------------------------------------------------")
print("************************************************************")
print("Bai 2")
import math
print("Nhap vao so x: = " )
x = float(input())
print("Nhap vao so y: = " )
y = float(input())
print("nhap vao so z: = " )
z = float(input())
F = (x + y + z)/(x * x + y * y + 1) - abs(x - z * math.cos(y))
print("Gia tri cua phep tinh F voi x = %s, y = %s, z = %s = %s" %(int(x), int(y), int(z), F))
print("************************************************************")
print("------------------------------------------------------------")
print("************************************************************")
print("Bai 3")
print("Nhap so a = ")
a = float(input())
print("Nhap so b = ")
b = float(input())
S = a + b
print("Tong 2 so a = %s va b = %s la %s" %(int (a), int(b), int(S)))
tru = a - b
print("Hieu 2 so a = %s va b = %s la %s" %(int (a), int(b), int(tru)))
nhan = a * b
print("Tich 2 so a = %s va b = %s la %s" %(int (a), int(b), int(nhan)))
chia  = a / b
print("Thuong 2 so a = %s va b = %s la %s" %(int (a), int(b), chia))
laydu = a % b
print("Lay du cua phep chia 2 so a = %s va b = %s la %s" %(int (a), int(b), int(laydu)))
layphannguyen = a // b
print("Lam tron xuong cua phep chia 2 so a = %s va b = %s la %s" %(int (a), int(b), int(layphannguyen)))
binhphuong = a ** b
print("Gia tri cua phep tinh so a = %s mu b = %s la %s" %(int (a), int(b), int(binhphuong)))
print("************************************************************")
