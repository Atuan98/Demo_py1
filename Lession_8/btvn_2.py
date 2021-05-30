def nhap():
	tuple_ = ()
	n = int(input("Hay nhap so luong phan tu cua tuple: "))
	i = 0
	while i < n:
		tuple_ += input("Nhap phan tu vao tuple: "),
		i += 1 
	return tuple_
def dao_nguoc(tuple_):
	print(f"{tuple(reversed(tuple_))}")

dao_nguoc(nhap())