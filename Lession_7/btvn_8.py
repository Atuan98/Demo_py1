def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		number = int(input("Hay nhap phan tu: "))
		if number >= 0:
			list_.insert(i,number)
		i += 1
	print(f"{list_}")
	return list_

def dem_so_luong(list_):
	if list_:
		i = 0
		j = len(list_) - 1
		dem = 0
		while i < len(list_):
			while j > i:
				if list_[i] > list_[j]:
					dem += 1
				j -= 1
			j = len(list_) - 1 
			i += 1
		print(f"Ket qua so luong phan tu thoa man: {dem}")
	else:
		print("List rong")


list_ = nhap()
dem_so_luong(list_)