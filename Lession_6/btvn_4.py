import math
def nhap():
	number = int(input("Hay nhap so de kiem tra: "))
	return number

def xuat(number, ket_qua):
	print(f"So {number} la so nguyen to: {ket_qua}")

def is_prime(number):
	if number == 2:
		return True
	if number % 2 == 0 or number < 2:
		return False 
	max_range = int(math.sqrt(number)) + 1
	for value in range(3, max_range , 2):
		if number % value == 0:
			return False
	return True

a = nhap()
b = is_prime(a)
xuat(a, b)