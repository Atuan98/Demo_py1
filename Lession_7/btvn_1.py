def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,float(input("Hay nhap thanh phan: ")))
		i += 1
	print(f"{list_}")
	return list_, n

def tong_tich(list_, n):
	tong = 0
	tich = 1
	i = 0
	if list_:
		while i < n:
			tong += list_[i]
			tich *= list_[i]
			i += 1
	else:
		print("List rong")
	return tong, tich

list__ = nhap()
print(f"Tong = {tong_tich(list__[0], list__[1])[0]}, Tich = {tong_tich(list__[0], list__[1])[1]}")
