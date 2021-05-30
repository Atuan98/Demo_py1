def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def them(list_):
	if list_:
		print(f"Nhap vi tri muon them vao (0 <= vitri < {len(list_)}): ")
		vitri = int(input(""))
		if 0 <= vitri < len(list_):
			chuoi = input("Nhap chuoi muon them: ")
			list_[vitri] += chuoi
		else:
			print(f"Khong co vitri = {vitri} trong list")
	else:
		print("List rong")
	return list_

m = nhap()
print(f"Ket qua: {them(m)}")