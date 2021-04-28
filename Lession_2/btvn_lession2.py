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
print('+++++++++++++++++++++++++++++++++++++++++')
a1 = 3101
print(a1, 'is type ', type(a1))
print(a1, 'is type bool? ', isinstance(a1, bool))
print('------------------------------------------------------')
b = 31.01
print(b, ' is type ', type(b))
print(b, ' is type int? ', isinstance(b, int))
print('+++++++++++++++++++++++++++++++++++++++++')
b1 = 19.98
print(b1, 'is type ', type(b1))
print(b1, 'is type float? ', isinstance(b1, float))
print('------------------------------------------------------')
c = 'I am robot'
print(c, ' is type ', type(c))
print(c, ' is type string? ', isinstance(c, str))
print('+++++++++++++++++++++++++++++++++++++++++')
c1 = 'I am student'
print(c1, ' is type ', type(c1))
print(c1, ' is type string? ', isinstance(c1, str))
print('------------------------------------------------------')
d = 10 + 3j
print(d, ' is type ', type(d))
print(d, ' is type complex? ', isinstance(d, complex))
print('+++++++++++++++++++++++++++++++++++++++++')
d1 = 40 + 0j
print(d1, ' is type ', type(d1))
print(d1, ' is type complex? ', isinstance(d1, complex))
print('------------------------------------------------------')
e = False
print(e, ' is type ', type(e))
print(e, ' is type bool? ', isinstance(e, bool))
print('+++++++++++++++++++++++++++++++++++++++++')
e = True
print(e, ' is type ', type(e))
print(e, ' is type bool? ', isinstance(e, bool))