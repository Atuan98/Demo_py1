def nhap():
	my_dict1 = {}
	my_dict2 = {}
	n1 = int(input("Hay nhap so luong phan tu dict 1: "))
	n2 = int(input("Hay nhap so luong phan tu dict 2: "))
	i = 0
	while i < n1:
		m1 = input("Hay nhap key dict 1: ")
		if my_dict1.get(m1) is None: 
			my_dict1[m1] = input("Hay nhap value dict 1:  ")
			i += 1
		else:
			my_dict1[m1] = input("Hay nhap value dict 1:  ")
	i = 0
	while i < n2:
		m2 = input("Hay nhap key dict 2: ")
		if my_dict2.get(m2) is None: 
			my_dict2[m2] = input("Hay nhap value dict 2:  ")
			i += 1
		else:
			my_dict2[m2] = input("Hay nhap value dict 2:  ")
	return my_dict1, my_dict2

def xuat(my_dict1, my_dict2):
	print(f"Dict 1: {my_dict1.item()}, Dict 2: {my_dict2.items()}")


m = nhap()
xuat(m[0],m[1])

