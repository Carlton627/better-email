## https://docs.python.org/3/library/secrets.html

class GenerateStrongPassword:
	def __init__(self):
		self.__password = None


	def password_generator(self, username):
		hashing_string = self.generate_random_string(username)
		ihashing_string = ""
		for unit in hashing_string:
			ihashing_string += unit 


	def generate_random_string(self, username):
		import secrets
		random_string = secrets.token_hex(32)
		return random_string
		

if __name__ == '__main__':
	email_id = "ethicaldeveloper627@gmail.com"
	username = email_id.split("@")[0]
	password_generator = GenerateStrongPassword()
	password_generator.password_generator(username)

