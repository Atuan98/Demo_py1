def nhap():
	str_ = input("Hay nhap vao 1 chuoi: ")
	return str_

def xuat(str_):
	my_dict = {}
	for i in str_:
		my_dict[i] = str_.count(i)
	print(my_dict) 

xuat(nhap())
