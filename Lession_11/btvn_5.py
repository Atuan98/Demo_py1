class NewString:
	def get_string(self):
		stri = input("Hay nhap gia tri: ")
		return stri
	def print_string(self, stri):	
		print(stri.upper())

ns = NewString()
ns.print_string(ns.get_string())