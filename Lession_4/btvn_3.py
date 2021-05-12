print("Bai 3")
tong = 0
while True:
	a = int(input("Hay nhap 1 so nguyen duong bat ki "))
	if a < 10:
		tong += a
		print(f"So da nhap la {a} co tong cac chu so = {tong}")
		tong = 0
	elif a < 100:
		tong += a//10 + a%10
		print(f"So da nhap la {a} co tong cac chu so = {tong}")
		tong = 0
	elif a < 1000:
		tong += a//100 + (a%100)//10 + ((a%100)%10)
		print(f"So da nhap la {a} co tong cac chu so = {tong}")
		tong = 0
	else:
		print("Ban da nhap so >= 1000. Vui long nhap lai")
		continue
