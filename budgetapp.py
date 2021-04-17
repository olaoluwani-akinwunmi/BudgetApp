class Budget:
	def __init__(self, category):
		self.category=category
		self.ledger=list()

	def __str__(self):
		title=f"{self.category:*^37}\n"
		items=""
		total=0
		for item in self.ledger:
			items += f"{item['description'][0:30]:30}" + f"{item['amount']:>7.2f}" + '\n'

			total += item['amount']

		output= title + items + "Balance: " + str(total)
		return output



	def deposit(self, amount, description=" "):
		self.ledger.append({"amount": amount, "description": description})


	def withdraw(self, amount, description=" "):
		if (self.check_funds(amount)):
			self.ledger.append({"amount": -amount, "description": description})
			return True;

		return False

	def get_balance(self):
		total_cash=0
		for item in self.ledger:
			total_cash += item['amount']

		return total_cash

	def transfer(self, amount, category):
		if (self.check_funds(amount)):
			self.withdraw(amount, "Transfer to " + category.category)

			category.deposit(amount, "Transfer from " + self.category)

			return True

		return False


	def check_funds(self, amount):
		if self.get_balance() >= amount:
			return True

		return False