def nhap():
	tuple_ = ()
	n = int(input("Hay nhap so luong phan tu cua tuple: "))
	i = 0
	while i < n:
		tuple_ += input("Nhap phan tu vao tuple: "),
		i += 1 
	return tuple_

def kiem_tra(tuple_):
	if tuple_:
		dem = 0
		m = tuple_[0]
		for ky_tu in tuple_:
			if ky_tu == m:
				dem +=1
		if dem == len(tuple_) :
			print("Tat ca phan tu trong tuple giong nhau")
		else:
			print("Phan tu trong tuple khong giong nhau")
	else:
		print("Tuple rong")

kiem_tra(nhap())