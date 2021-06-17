class MyClass:
	atr = 0

	def func(self):
		print(f"Hi {self}")


gr = MyClass()
print(gr.__class__.__name__)