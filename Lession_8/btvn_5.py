def nhap():
	n = int(input("Nhap so luong cua list: "))
	m = int(input("Hap nhap so luong phan tu cua tuple: "))
	i = 0
	j = 0
	list_1 = []
	tuple_ = ()
	while i < n:
		while j < m:
			number = input(f"Tuple [{i}][{j}]: "),
			tuple_ += number
			j += 1
		list_1.insert(i,tuple_)
		i += 1
		tuple_ = ()
		j = 0 
	print(f"{list_1}")
	return list_1

def min_(list_1):
	for ky_tu in list_1:
		if len(ky_tu) > 1:
			min_ = ky_tu[1]
			giatri_1 = ky_tu
			break
	for giatri in list_1:
		if len(giatri) > 1:
			if giatri[1] < min_:
				min_ = giatri[1]
				giatri_1 = giatri
	print(f"Tuple co gia tri nho nhat la {giatri_1}")
m = nhap()
min_(m)
