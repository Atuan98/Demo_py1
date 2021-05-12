print("Bài 2")
import math
x = float(input("Nhập vào số x = "))
n = int(input("Nhập vào số n = "))
if n < 0:
	print("Cần phải nhập số n là số nguyên dương ")
else:
	S_1 = 1
	S_2 = 1
	S_3 = 1
	dem = 1
	giaithua = 1
	for i in range(1, n + 1):
		S_1 += x ** i
		S_2 += (-1) ** i * x ** i
		if i == 2:
			giaithua = 2
		else:
			while dem <= i:
				giaithua *= dem 
				dem += 1
		S_3 += (x ** i)/giaithua
		dem = 1
		giaithua = 1
	print(f"S_1 = {S_1}")
	print(f"S_2 = {S_2}")
	print(f"S_3 = {S_3}")
