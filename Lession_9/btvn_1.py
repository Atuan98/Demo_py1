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

def min_max(my_dict):
	for i in my_dict:
		max_ = my_dict[i]
		min_ = my_dict[i]
		for i_ in my_dict:
			if my_dict[i_] > max_:
				max_ = my_dict[i_]
			elif my_dict[i_] < min_:
				min_ = my_dict[i_]
		break
	print(f"Max = {max_}, Min = {min_}")

min_max(nhap())