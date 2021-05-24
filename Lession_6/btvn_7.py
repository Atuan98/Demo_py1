def nhap():
	h = float(input("Hay nhap chieu cao: "))
	m = float(input("Hay nhap khoi luong: "))
	return h, m

def body_mass_index(chiso):
	bmi = chiso[1] / (chiso[0] ** 2)
	return bmi

def bmi_information(chiso, bmi):
	if bmi < 18.5:
		print(f"Nguoi co chieu cao: {chiso[0]}, can nang: {chiso[1]} co chi so bmi la {bmi} < 18,5 bi qua gay")
	elif 18.5 <= bmi <= 24.9:
		print(f"Nguoi co chieu cao: {chiso[0]}, can nang: {chiso[1]} co chi so bmi la 18,5 <= {bmi} <= 24,9 la nguoi binh thuong")
	elif 25 <= bmi < 29.9:
		print(f"Nguoi co chieu cao: {chiso[0]}, can nang: {chiso[1]} co chi so bmi la 25 <= {bmi} <= 29,9 bi qua can")
	elif 30 <= bmi < 34.9:
		print(f"Nguoi co chieu cao: {chiso[0]}, can nang: {chiso[1]} co chi so bmi la 30 <= {bmi} <= 34,9 bi beo phi")
	else:
		print(f"Nguoi co chieu cao: {chiso[0]}, can nang: {chiso[1]} co chi so bmi la  {bmi} > 35 bi qua beo phi")

a = nhap()
b = body_mass_index(a)
bmi_information(a,b)