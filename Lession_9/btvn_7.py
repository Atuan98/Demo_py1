# Sap xep theo chuoi
def nhap():
	my_dict = {}
	n = int(input("Hay nhap so luong phan tu dict: "))
	i = 0
	while i < n:
		m = input("Hay nhap key: ")
		if my_dict.get(m) is None: 
			my_dict[m] = input("Hay nhap value ")
			i += 1
		else:
			my_dict[m] = input("Hay nhap value ")
	return my_dict

def sapxep(my_dict):
	dem = 0
	print(sorted(my_dict.values(),reverse= True))
	for i in sorted(my_dict.values(), reverse= True):
		dem += 1
		if dem <= 3:
			print(i)
		else:
			break

sapxep(nhap()) 