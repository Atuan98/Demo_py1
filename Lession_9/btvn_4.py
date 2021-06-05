def nhap():
	my_dict = {}
	my_list = []
	n = int(input("Hay nhap so luong phan tu dict: "))
	i = 0
	i_ = 0
	if n > 2:
		while i < n:
			m = input("Hay nhap key: ")
			if my_dict.get(m) is None:
				number_list = int(input("Hay nhap so luong phan tu list trong dict: "))
				if number_list > 4:
					while i_ < number_list:
						my_list.insert(i_, input("Hay nhap phan tu vao list: "))
						i_ += 1
				else:
					print("So luong phan tu list < 5")
					break
				my_dict[m] = my_list
				my_list = []
				i_ = 0
				i += 1
			else:
				my_dict[m] = input("Hay nhap value ")
	else:
		print("So luong phan tu < 3")
	return my_dict


def in_phantu_5(my_dict):
	tuple_ = ()
	for x in my_dict.values():
		tuple_ += x,
	for y in range(len(tuple_)):
		print(f"Phan tu thu 5: {tuple_[y][4]} trong value vi tri thu {y}")


in_phantu_5(nhap())