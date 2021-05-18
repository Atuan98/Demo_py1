s = input("Nhập chuỗi s: ")
b = ""
for i in range(len(s)):
	if i % 2 == 0:
		b += s[i]
	else:
		continue
print(f"Chuỗi đã xóa những kí tự có chỉ số lẻ là {b}")

