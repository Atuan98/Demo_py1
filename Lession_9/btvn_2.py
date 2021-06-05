def nhap():
	my_dict = {}
	n = int(input("Hay nhap so luong phan tu dict: "))
	i = 0
	while i < n:
		m = input("Hay nhap key: ")
		if my_dict.get(m) is None: 
			my_dict[m] = input("Hay nhap value ")
			i += 1
		else:
			my_dict[m] = input("Hay nhap value ")
	return my_dict

def giatri_khongtrunglap(my_dict):
	tuple_ = ()
	for x in my_dict.values():
		tuple_ += x,
	for y in tuple_:
		if tuple_.count(y) == 1:
			print(f"Gia tri khong trung lap la: {y}")

giatri_khongtrunglap(nhap())

