def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def dem_so(list_):
	if list_:
		i = 0
		dem = 0
		while i < len(list_):
			if len(list_[i]) >= 2:
				if list_[i][0] == list_[i][len(list_[i]) - 1]:
					dem += 1
			i += 1
		print(f"So chuoi: {dem}")	
	else:
		print("List rong")

m = nhap()
dem_so(m)