
def nhap():
	str = input("Hay nhap chuoi : ")
	return str

def change_upper_lower(str):
	str = str.swapcase()
	return str

def xuat(str):
	print(f"Chuoi da thay doi: {str}")

a = nhap()
b = change_upper_lower(a)
xuat(b)