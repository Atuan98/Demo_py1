s = input("Hãy nhập chuỗi s: ")
a = ""
b = ""
_min = ord(s[0])
_max = ord(s[0])
for ky_tu in s:
	if ord(ky_tu) <= _min:
		_min  = ord(ky_tu)
		a = ky_tu
	elif ord(ky_tu) > _max:
		_max = ord(ky_tu)
		b = ky_tu
print(f"Ký tự nhỏ nhất là {a} có giá trị là {_min},Ký tự lớn nhất là {b} có giá trị là {_max}")