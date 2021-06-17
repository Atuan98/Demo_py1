class Dog:
	species = 'animal'

	def __init__(self, name, age):
		self.name = name  
		self.age = age  

def get_biggest_number(*args):
	max_ = args[0]
	print(args)
	for i in args:
		if i > max_:
			max_ = i
	print(f"The oldest dog is {max_} year old")


dog1 = Dog('Fake', 2)
dog2 = Dog('Mickey', 7)
dog3 = Dog('Fuk', 5)

get_biggest_number(dog1.age,dog2.age,dog3.age)