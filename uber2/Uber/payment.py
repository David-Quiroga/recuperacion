from user import User
from driver import Driver

class Payment:
	ide			=	int
	ammount		=	int
	user		=	User("", "", "", "", "", "", "", "")
	driver      =   Driver("", "", "", "", "", "", "", "", "", "")
	tipo		=	str
	
	def __init__(self, ide, ammount,user,driver,tipo):
		self.ide		=	ide
		self.ammount	=	ammount
		self.user		=	user
		self.driver		=	driver
		self.tipo		=	tipo

