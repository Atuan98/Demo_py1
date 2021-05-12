print("Bài 1")
import math
a = float(input("Nhập vào số a = "))
b = float(input("Nhập vào số b = "))
c = float(input("Nhập vòa số c = "))
if a == 0:
	print(f"Nghiệm của phương trinh {int(b)}x + {int(c)} là: {-c/b}")
else:
	lamda = b**2 - 4*a*c
	if lamda < 0:
		print("Phương trình vô nghiệm")
	elif lamda == 0:
		print(f"Nghiệm của phương trình {int(a)}x^2 + {int(b)}x + {int(c)} là nghiệm kép: {-b/(2*a)}")
	else:
		x1 = (-b + math.sqrt(b**2 - 4 * a * c))/2*a
		x2 = (-b - math.sqrt(b**2 - 4 * a * c))/2*a
		print(f"Nghiệm của phương trình {int(a)}x^2 + {int(b)}x + {int(c)} là x1 = {int(x1)}, x2 = {int(x2)}")
    	
