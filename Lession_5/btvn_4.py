s = input("Nhập vào chuỗi s: ")
if len(s) < 2:
	print("Chuỗi rỗng")
else:
	print(f"Chuỗi s_1 = {s[0:2]} và s_2 = {s[len(s)-2:len(s)]}")