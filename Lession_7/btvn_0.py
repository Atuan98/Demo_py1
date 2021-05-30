import random
def nhap():
	n = int(input("Hay nhap so phan tu cua list: "))
	i = 0
	list_ = []
	while i < n:
		list_.insert(i,input("Hay nhap thanh phan: "))
		i += 1
	print(f"{list_}")
	return list_

def random_(list_): 
	if  0 < len(list_) < 5:
		print(f"Chuoi: {list_}")
	elif len(list_) > 5:
		print(f"Chuoi random: {random.sample(list_,k = 5)}")
	else:
		print("List rong")

n = nhap()
random_(n)