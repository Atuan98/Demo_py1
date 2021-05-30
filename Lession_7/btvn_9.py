def nhap():
	i = 0
	j = 0
	list_1 = []
	list_1_ = []
	while i < 3:
		while j < 3:
			number = float(input(f"List 1[{i}][{j}]: "))
			list_1_.insert(j, number)
			j += 1
		list_1.insert(i,list_1_)
		i += 1
		list_1_ = []
		j = 0 

	print(f"{list_1[0]}")
	print(f"{list_1[1]}")
	print(f"{list_1[2]}")

	i = 0 
	j = 0
	list_2 = []
	list_2_ = []
	while i < 3:
		while j < 3:
			number = float(input(f"List 2[{i}][{j}]: "))
			list_2_.insert(j,number)
			j += 1
		list_2.insert(i,list_2_)
		i += 1
		list_2_ = []
		j = 0 

	print(f"{list_2[0]}")
	print(f"{list_2[1]}")
	print(f"{list_2[2]}")
	return list_1, list_2

def tinh_tich(list_1, list_2):
	list_moi = []
	list_moi_ = []
	i = 0
	j = 0
	m = 0
	n = 0 
	number = 0
	while i < 3:
		while j < 3:
			while m < 3:
				number += list_1[i][m] * list_2[m][j]
				m += 1
			list_moi_.insert(j,number)
			j +=1
			m = 0
			number = 0
		i += 1
		list_moi.insert(i,list_moi_)
		j = 0
		m = 0
		number = 0
		list_moi_ = []
	print(f"{list_moi[0]}")
	print(f"{list_moi[1]}")
	print(f"{list_moi[2]}")

m = nhap()
tinh_tich(m[0], m[1])