import math

def nhap():
	number = int(input("Hay nhap so de kiem tra: "))
	return number

def xuat(number):
	print(f"So {number} la so hoan hao")

def kiem_tra_so_nguyen_to(number):
	if number == 2:
		return True
	if number % 2 == 0 or number < 2:
		return False 
	max_range = int(math.sqrt(number)) + 1
	for value in range(3, max_range , 2):
		if number % value == 0:
			return False
	return True

def is_perfect(number):
	number = str(number)
	if number == '6':
		return number
	elif number[len(number) - 1] == '6' or number[len(number) - 1] == '8':
		number = int(number)
		max_range = int(math.sqrt(number))
		for value in range(max_range, number):
			for so in range(1, int(value / 2)):
				so_nguyen_to = (value ** so) -1
				if number % so_nguyen_to == 0 and (number / so_nguyen_to) % 2 == 0:
					if kiem_tra_so_nguyen_to(so_nguyen_to) == True:
						return number


a = nhap()
b = is_perfect(a)
xuat(b)