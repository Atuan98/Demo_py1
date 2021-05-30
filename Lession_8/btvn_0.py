def nhap():
	tuple_ = ()
	n = int(input("Hay nhap so luong phan tu cua tuple: "))
	i = 0
	while i < n:
		tuple_ += input("Nhap phan tu vao tuple: "),
		i += 1 
	return tuple_

def un_pack(tuple_):
	for i in range(len(tuple_)):
		print(f"{tuple_[i]}")

m = nhap()
un_pack(m)