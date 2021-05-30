def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		number = int(input("Hay nhap phan tu: "))
		if number >= 1:
			list_.insert(i,number)
		i += 1
	#print(f"{list_}")
	return list_

def sap_xep(list_):
	set_moi = set()
	for ky_tu in list_:
		set_moi.add(ky_tu)
	list_moi = list (set_moi)
	return print(f"{list_moi}")


str_ = nhap()
sap_xep(str_)