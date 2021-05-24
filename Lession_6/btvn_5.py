def nhap():
	str = input("Hay nhap so de kiem tra: ")
	return str

def xuat(str, count_upper_lower):
	print(f"Chuoi {str} co so phan tu viet hoa la {count_upper_lower[1]}, viet thuong la {count_upper_lower[0]}")

def count_upper_lower(str):
	count_lower = 0
	count_upper = 0
	for i in range(len(str)):
		if str[i].islower() == True:
			count_lower += 1
		else:
			count_upper += 1
	return count_lower, count_upper

a = nhap()
b = count_upper_lower(a)
xuat(a,b)

