def nhap():
	n = int(input("Hay nhap so phan tu cua tuple 1: "))
	m = int(input("Hay nhap so phan tu cua tuple 2: "))
	i = 0
	tuple_1 = ()
	tuple_2 = ()
	while i < n:
		tuple_1 += input("Hay nhap thanh phan tuple_1: "),
		i += 1
	i = 0
	while i < m:
		tuple_2 += input("Hay nhap thanh phan tuple_2: "),
		i += 1
	print(f"{tuple_1}")
	print(f"{tuple_2}")
	return tuple_1, tuple_2

def kiem_tr(tuple_1, tuple_2):
	if tuple_1 and tuple_2:
		i = 0 
		dem = 0
		while i < len(tuple_1):
			if tuple_1[i] in tuple_2:
				dem += 1
			i += 1
		if dem > 0:
			print(f"2 tuple co {dem} phan tu chung ")
		else:
			print("2 tuple khong co phan tu chung")
	else:
		print("List rong")


m = nhap()
kiem_tr(m[0], m[1])