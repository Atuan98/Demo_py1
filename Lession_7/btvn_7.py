def nhap():
	n = int(input("Hay nhap so phan tu cua list 1: "))
	m = int(input("Hay nhap so phan tu cua list 2: "))
	i = 0
	list_1 = []
	list_2 = []
	while i < n:
		list_1.insert(i,input("Hay nhap thanh phan list_1: "))
		i += 1
	i = 0
	while i < m:
		list_2.insert(i,input("Hay nhap thanh phan list_2: "))
		i += 1
	print(f"{list_1}")
	print(f"{list_2}")
	return list_1, list_2

def kiem_tr(list_1, list_2):
	if list_1 and list_2:
		i = 0 
		dem = 0
		while i < len(list_1):
			if list_1[i] in list_2:
				dem += 1
			i += 1
		if dem > 0:
			print(f"2 chuoi co {dem} phan tu chung ")
		else:
			print("2 chuoi khong co phan tu chung")
	else:
		print("List rong")


m = nhap()
kiem_tr(m[0], m[1])