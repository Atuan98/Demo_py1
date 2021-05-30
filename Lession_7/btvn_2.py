def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def max_min(list_):
	return max(list_), min(list_)

m = nhap()
print(f"Max = {max_min(m)[0]}, Min = {max_min(m)[1]}")