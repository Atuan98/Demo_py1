def nhap():
	my_dict = {}
	n = int(input("Hay nhap so luong phan tu dict: "))
	i = 0
	while i < n:
		m = input("Hay nhap key: ")
		if my_dict.get(m) is None: 
			my_dict[m] = int(input("Hay nhap value "))
			i += 1
		else:
			my_dict[m] = int(input("Hay nhap value "))
	return my_dict

def tich(my_dict):
	tong  = 1
	for i in my_dict:
		tong  *= my_dict[i]
	print(f"Tong = {tong}")

tich(nhap())