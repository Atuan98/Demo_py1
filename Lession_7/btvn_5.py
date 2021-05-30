
def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def dem_so_lan(list_):
	if list_:
		max_ = list_.count(list_[0])
		giatri = list_[0]
		i = 1
		while i < len(list_):
			if max_ < list_.count(list_[i]):
				max_ = list_.count(list_[i])
				giatri = list_[i]
			i += 1
		print(f"Phan tu {giatri} co so lan lap nhieu nhat la {max_}")
	else:
		print("List rong")

m = nhap()
dem_so_lan(m)