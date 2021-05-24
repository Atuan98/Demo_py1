def nhap():
	n = int(input("Hay nhap so luong phan tu: "))
	i = 0
	number = []
	while i < n:
		number += [int(input("Hay nhap cac gia tri: "))]
		i += 1
	print(f"Day so da nhap = {number}")
	return number

def max_min(*number):
	max_ = number[0]
	max__ = max_[0]
	min__ = max_[0]
	for so in max_:
		if so > max__:
			max__ = so
		elif so < min__:
			min__ = so
	return max__, min__


s = nhap()
_max__, _min__ = max_min(s)
print(f"Max = {_max__}, Min = {_min__}")