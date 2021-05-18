s = input("Nhập chuỗi s: ")
m = int(input("Nhập giá trị m: "))
if s == "":
	print(f"Chuỗi s = {s} là chuỗi rỗng")
elif m < 0 or m > len(s) - 1:
	print(f"Giá trị m = {m} < 0 hoặc giá trị m = {m} vượt quá độ dài chuỗi")
else:
	s = s[0: m] + s[m+1:]
	print(f"Chuỗi đã cắt là {s}")