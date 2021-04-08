from datetime import datetime

allowedUsers = ["Seyi", "Mike", "Love"]
allowedPassword = ["passwordSeyi", "PasswordMike", "passwordLove"]
name = input("What is your name ? \n")

if (name in allowedUsers):
	password = input("Type in your pasword:  ")
	userId = allowedUsers.index(name)

	if (password == allowedPassword[userId]):
		timeLoggedIn = datetime.now()
		dt_string = timeLoggedIn.strftime("%d/%m/%Y %H:%M:%S")

		print(f"\n Welcome {name};")
		print(f"{dt_string}\n\n")
		print("These are the available options: ")
		print("1. Withdrawal")
		print("2. Cash Deposit")
		print("3. Complaint") 

		selectedOption = int(input("Please select an option: "))

		if (selectedOption == 1):
			#print(f"You selected {selectedOption}\n")
			cashOut = int(input("How much would you want to recieve ?\n"))
			print("Take your cash.")

		elif (selectedOption == 2):
			currentBalance = 1000
			#print(f"You selected {selectedOption}\n")
			deposit = int(input("How much would you like to deposit ?\n"))
			currentBalance += deposit
			print(f"Your current balance is: N{currentBalance}")


		elif (selectedOption == 3):
			#print(f"You selected {selectedOption}")
			complaint = input("What issue would you like to report ?\n")
			print("Thank you for contacting us.")

		else:
			print("Invalid option selcted, please try again.")

	else:
		print("Password incorrect, please try again.")
else:
	print("Name not found, please try again.")