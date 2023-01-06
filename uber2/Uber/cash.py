from payment import Payment

class Cash(Payment):
	
	def __init__(self, ide, ammount,user,driver,tipo):
		super().__init__(ide, ammount,user,driver,tipo)