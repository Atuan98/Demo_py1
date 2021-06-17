class pet:
	class dog:
		species = 'mammals'
		is_hurry = True
		def __init__(self, name, age):
			self.name = name 
			self.age = age 
		def eat(self):
			self.is_hurry = False

def in_ra(species,*args):
	print(f"I have {int((len(args))/2)} dogs")
	print(f"{args[0]} is {args[4]}. {args[1]} is {args[5]}. {args[2]} is {args[6]}. {args[3]} is {args[7]} ") 	
	print(f"And they're all {species}, of course")

def in_ra1(*args):
	k = 0
	for i in args:
		if i == True:
			print("My dogs are hurry")
			break
		else:
			k += 1 
	if  k == len(args):
		print("My dogs are not hurry")

dog1 = pet().dog('Tom', 6)
dog1.eat()
dog2 = pet().dog('Jerry', 9)
dog2.eat()
dog3= pet().dog('Butt', 3)
dog3.eat()
dog4 = pet().dog('Wine', 1)
dog4.eat()

in_ra(dog1.species,dog1.name, dog2.name, dog3.name, dog4.name, dog1.age, dog2.age, dog3.age, dog4.age)
in_ra1(dog1.is_hurry,dog2.is_hurry, dog3.is_hurry, dog4.is_hurry)
