class Accountmanager:

	def __init__(self,account_name,account_no,balance,pin):
		self.account_name=account_name
		self.account_no=account_no
		self.balance=float(balance)
		self.pin=pin
		self.transactions=[]

	def deposit(self,amount=0.0):
		if amount>10000:
			print("you can't add more than 10000")
		elif amount<0:
			print("invalid amount")
		else:
			self.balance+=amount
			transaction=('+'+str(amount),self.balance)
			self.transactions.append(transaction)

	def withdraw(self,amount=0.0):
		if (self.balance-amount)<0:
			print("insufficient balance")
		elif self.balance<=3000:
			print("low balance")
		else:
			self.balance-=amount
			transaction=('-'+str(amount),self.balance)
			self.transactions.append(transaction)
		

	def show_balance(self):
		print(f"total balance:{self.balance}")

	def account_statement(self):
		return self.transactions