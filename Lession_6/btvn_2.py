def reverse_string(str):
	_str = str[::-1]
	return _str

def nhap():
	str = input("Hay nhap chuoi: ")
	return str

def xuat(_str):
	print(f"Chuoi dao nguoc la: {_str}")

s = nhap()
s1 = reverse_string(s)
xuat(s1)
