#BÀI TẬP VỀ NHÀ
'''
Bài 01. Trong lập trình python
    - Đặt 5 tên biến đúng quy tắc
    - Đặt 10 tên biến sai quy tắc
Bài 02.
    - Theo bài học thì có mấy kiểu dữ liệu?
    - Ứng với mỗi kiểu đó, hãy khai báo 2 biến và dùng lệnh print để in ra màn hình
'''
#Bài làm
'''
Bài 01.
	- Tên biến đúng quy tắc: __str__; __A; ANHTUAN; anhtuan; anh_tuan
	- Tên biến sai quy tắc: and, 09; 123A; while; True; False; try; or; with; not
Bài 02.
	- Có 2 kiểu dữ liệu
		+ Kiểu dữ liệu dựng sẵn
			- Số: int, float, complex
			- Chuỗi, kí tự: string
			- bool
			- squence, set....
		+ Kiểu dữ liệu người dùng định nghĩa
'''
a = 1998
print(a, 'is type ', type(a))
print(a, 'is type int? ', isinstance(a, int))
print('------------------------------------------------------')
b = 31.01
print(b, ' is type ', type(b))
print(b, ' is type int? ', isinstance(b, int))
print('------------------------------------------------------')
c = 'I am robot'
print(c, ' is type ', type(c))
print(c, ' is type string? ', isinstance(c, str))
print('------------------------------------------------------')
d = 10 + 3j
print(d, ' is type ', type(d))
print(d, ' is type complex? ', isinstance(d, complex))
print('------------------------------------------------------')
e = False
print(e, ' is type ', type(e))
print(e, ' is type bool? ', isinstance(e, bool))