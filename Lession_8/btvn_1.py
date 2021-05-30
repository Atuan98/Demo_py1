def nhap():
	tuple_ = ()
	list_ = []
	n = int(input("Hay nhap so luong phan tu cua tuple va list: "))
	i = 0
	while i < n:
		tuple_ += input("Nhap phan tu vao tuple: "),
		list_.insert(i, input("Nhap phan tu vao list: "))
		i += 1 
	print(f"{tuple_}")
	print(f"{list_}")
	return tuple_, list_

def chuyen_doi(tuple_, list_):
	print(f"Tuple chuyen doi sang list: {list(tuple_)}")
	print(f"List chuyen doi sang tuple: {tuple(list_)}")

m = nhap()
chuyen_doi(m[0], m[1])
