import string
def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_
def in_ten_mien(list_):
	list_moi = []
	i = 0
	if list_:
		for ky_tu in list_:
			ky_tu = ky_tu[::-1]
			list_moi.insert(i,ky_tu[0:ky_tu.index(".")][::-1])
			i+= 1
		print(f"Cac hau to {list_moi}")
	else:
		print("Chuoi rong")
in_ten_mien(nhap())