print("Bai 5")
a = float(input("Hay nhap epsilon = "))
giaithua = 1
dem = 1 
e = 1
n = int(input("Hay nhap so n = "))
if a < 1:
	for i in range (1, n+1):
		if i == 2:
			giaithua = 2
		else:
			while dem <= i:
				giaithua *= dem 
				dem += 1
		e += 1/giaithua
		if 1/giaithua < a:
					print(f"Voi epsilon = {a}, n = {n} ket qua e = {e}")
					break
		dem = 1
		giaithua = 1
else:
	print("Nhap sai epsilon. Epsilon phai < 1")