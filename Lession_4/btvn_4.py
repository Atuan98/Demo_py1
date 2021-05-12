print("Bai 4")
while True:
	a = float(input("Nhap vao canh a = "))
	b = float(input("Nhap vao canh b = "))
	c = float(input("Nhap vao canh c = "))
	if a + b > c and a + c > b and b + c > a:
		print(f"3 canh a = {int(a)}, b = {int(b)}, c = {int(c)} la 3 canh cua tam giac")
		if a ==  b == c:
			print("Tam giac deu")
		elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
			print("Tam giac vuong")
		elif a == b or b == c or c == a:
			print("Tam giac can")
		elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
			print("Tam giac tu")
		else:
			print("Tam giac nhon")
	else:
		print(f"3 canh a = {int(a)}, b = {int(b)}, c = {int(c)} khong phai la 3 canh cua 1 tam giac")
