s = input("Nhập vào chuỗi s: ")
a = s[0]
b = ''
for ky_tu in s:
	if ky_tu == a:
		ky_tu = '$'
	b += ky_tu
print(f"Chuỗi đã thay đổi là {b}")