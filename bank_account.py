class bank_account:

	def __init__(self,owner,balance):
		
		self.owner = owner
		self.balance = balance
		
	def deposit(self,amt):
		self.balance += amt
		print("Hi {}, you deposited ${} in your account. Your current balance is ${}.".format(self.owner,amt,self.balance))
		
	def withdraw(self,amt):
		if amt <= self.balance:
			self.balance -= amt
			print("Hi {}, you withdrew ${} from your account. Your current balance is ${}.".format(self.owner,amt,self.balance))
		else:
			print("Sorry {}, you have less than the amount entered currently in your account.".format(self.owner))

	def __str__(self):
		return f"Account Owner: {self.owner} \nAccount Balance: {self.balance}"


acct1 = bank_account('Justyn',200)
print(acct1)
acct1.deposit(50)
acct1.withdraw(24)			