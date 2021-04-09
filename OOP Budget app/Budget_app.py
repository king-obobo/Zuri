class Budget:
    def __init__(self, category, availableBalance = 0):
        self.category = category
        self.availableBalance = availableBalance


    def deposit(self, amountToDeposit):
        amountToDeposit = int(amountToDeposit)
        self.availableBalance += amountToDeposit
        print("Deposit Successful !")
        print(f"You deposited ${amountToDeposit} to {self.category} Budget\n")



    def withdraw(self, amountToWithdraw):
        amountToWithdraw = int(amountToWithdraw)

        if (amountToWithdraw > 0) and (amountToWithdraw <= self.availableBalance):
            self.availableBalance -= amountToWithdraw
            print("Witdraw successful !")
            print(f"You have withdrawn ${amountToWithdraw} from {self.category} Budget\n")
        else:
            print("Insufficient Balance.\n")


    def checkBalance(self):
        print(f"Your available Balance in the {self.category} budget is: ${self.availableBalance}\n")


    def transferFunds(self, amountToTransfer, categoryToTransferTo):
        amountToTransfer = int(amountToTransfer)
        categoryToTransferTo.deposit(amountToTransfer)
        self.availableBalance -= amountToTransfer
        print("Transfer Success !")
        print(f"You transferred ${amountToTransfer} from {self.category} Budget to {categoryToTransferTo.category} Budget\n")



# food = Budget('food')
# food.deposit(200)
# food.withdraw(100)
# food.checkBalance()

# cloth = Budget("cloth")
# cloth.deposit(6000)
# cloth.transferFunds(2000, food)
# cloth.withdraw(1000)

# food.checkBalance()
# cloth.checkBalance()