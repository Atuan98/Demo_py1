def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def chia_chuoi(list_):
	if list_:
		print(f"Hay nhap n (0 <= n < {len(list_): })")
		n = int(input())
		if 0 <= n < len(list_):
			print(f"Chuoi 1 = {list_[0 : n + 1]}, Chuoi 2 = {list_[n+1 : len(list_)]}")
		else:
			print(f"Khong co vi tri = {n} trong list")
	else:
		print("List rong") 

m = nhap()
chia_chuoi(m)