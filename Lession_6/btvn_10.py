def nhap():
	number = int(input("Hay nhap so n: "))
	return number

def dequy(number):
	if 0 < number <= 2:
		return 1
	elif number == 0:
		return 0
	else:
		return dequy(number - 1) + dequy(number - 2)

def khongdequy(number):
	a1 = 1 
	a2 = 1
	i = 3
	a = 0
	if number == 1 or number == 2:
		a = 1
	elif number == 0:
		a = 0
	while i <= number:
		a = a1 + a2
		a1 = a2 
		a2 = a
		i += 1
	return a 

def xuat(a, b):
	print(f"Gia tri cua day fibonaci khong de quy: {b} ")
	print(f"Gia tri cua day fibonaci de quy: {a}")

number = nhap()
a = dequy(number)
b = khongdequy(number)
xuat(a,b)

