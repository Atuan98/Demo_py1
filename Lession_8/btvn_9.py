def nhap():
	tuple_ = ()
	n = int(input("Hay nhap so luong phan tu cua tuple: "))
	i = 0
	while i < n:
		tuple_ += float(input("Nhap phan tu vao tuple: ")),
		i += 1 
	return tuple_


def tinh_tong(tuple_):
	if tuple_:
		tong = 0
		for ky_tu in tuple_:
			tong += ky_tu
		print(f"Tong = {tong}, Max = {max(tuple_)}")
	else:
		print("Tuple rong")

tinh_tong(nhap())