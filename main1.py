from bank import Accountmanager
accounts={}
account_no=1001
print("-"*50)
print("welcome to Iron Bank")

while True:
	print("hey! What would you like to do today?\n\n\ 
		1.create an account\n\
		2.check balance\n\
		3.deposite amount\n\
		4.withdraw amount\n\
		5.exit\n\
		6.show balance\n")
	choice=int(input("enter your option:"))

	if choice==1:
		acc_name=input("enter the account name:")
		balance=input("enter the opening balance:")
		pin=int(input("enter a pin:"))

		accounts[account_no]=Accountmanager(acc_name,account_no,balance,pin)
		print(accounts)
		print(f"account created successfully! Your account no is:{account_no}")
		account_no +=1

	elif choice==2:
		acc_no=eval(input("enter account number:"))
		upin=eval(input("enter the pin for your account:"))

		if upin==accounts[acc_no].pin:
			statement=accounts[acc_no].account_statement()
			print(statement[0][0],statement[0][1],sep=" -- ")
		else:
			print("invalid")

	elif choice==3:
		acc_no=eval(input("enter account number:"))
		upin=eval(input("enter the pin for your account:"))

		if upin==accounts[acc_no].pin:
			amount
