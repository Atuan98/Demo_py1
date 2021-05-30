def nhap():
	tuple_ = ()
	n = int(input("Hay nhap so luong phan tu cua tuple: "))
	i = 0
	while i < n:
		tuple_ += input("Nhap phan tu vao tuple: "),
		i += 1 
	print(f"{tuple_}")
	return tuple_

def in_phan_tu_thu_4(tuple_):
	if tuple_ and len(tuple_) >= 4:
		print(f"Phan tu thu 4: {tuple_[3]}")
		print(f"Phan tu thu 4 tu duoi len: {tuple_[-4]}")
	else:
		print("So luong phan tu cua tuple < 4")

in_phan_tu_thu_4(nhap())