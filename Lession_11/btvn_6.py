class User:
	
	def __init__(self, first_name, last_name, birthday, email, address, user_name, password):
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
		self.email = email
		self.address = address
		self.user_name = user_name
		self.password = password

	def update_info(self, first_name, last_name, birthday, email, address, user_name, password):
		self.first_name = first_name
		self.last_name = last_name
		self.birthday = birthday
		self.email = email
		self.address = address
		self.user_name = user_name
		self.password = password

	def login(self, user_name, password):
		if user_name == self.user_name and password == self.password:
			print("Login sucess!")
		else:
			print("Error!")

	def logout(self):
		print("Logout!")

user = User('Acv', 'BxZX', 'Czxc', 'Dwq', 'Evv', 'Fwef','UHI')
user.update_info('AS', 'asd', 'asdqw', 'as', 'asd', 'asd', 'q')
print(user.first_name)
