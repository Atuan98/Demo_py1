
def nhap():
	number = int(input("Hay nhap so de kiem tra: "))
	return str(number)

def dequy(number, i):
	if i == len(number):
	 	return 0 
	if int(number) >= 0:
		if int(number[i]) % 2 != 0:
			return 1 +  dequy(number ,i + 1)
		else:
			return dequy(number ,i + 1)
	else:
			return print(f"So {number} khong phai la nguyen duong")

a = nhap()
i = 0
print(f"{dequy(a,i)}")

