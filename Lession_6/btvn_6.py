import string
def nhap():
	str = input("Hay nhap chuoi de kiem tra: ")
	return str

def is_pangram(str, alphabet):
	i = 0
	for ky_tu in alphabet:
		if ky_tu in str:
			i += 1
	if i == 26:
		print(f"Chuoi {str} la pangram")
	else:
		print(f"Chuoi {str} khong la pangram")

b = string.ascii_lowercase
a = nhap()
is_pangram(a,b)
			