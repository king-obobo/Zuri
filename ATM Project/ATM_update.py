# A simple ATM project implemented using codes.
# More updates would be done as I proceed, especially writing database to a local file upon termination of application
# Checking if account number generated already exists in the database, and if it does then simply generate another account number


from datetime import datetime
from os import system
import random

balance = 0
### A local database to test the functionality.
database = {1111:{"first_name": "Ebuka", "last_name": "Obobo", "email": 'ebuka@gmail.com', "password": "1111", "balance": balance},
            2222:{"first_name": "Tobiu", "last_name": "Obobo", "email": "tobiuo@gmail.com", "password": "2222", "balance": balance}
            }

### A Simple welcome function
def welcome():
    print("""
        ******************
        Welcome to BankPHP
        ******************
    """)


# A simple Login function, would only login if the data exists in the local database
def login():
    print("""*********Login Page**********
    Kindly provide your details to Login
    """)
    
    accountNumberFromUser = int(input("Type in your account Number: "))
    passFromUser = input("Type in your Password: ")

    if (accountNumberFromUser in database.keys()) and (database[accountNumberFromUser]["password"] == passFromUser):
        timeLoggedIn = datetime.now()
        dt_string = timeLoggedIn.strftime("%d-%m-%Y %H:%M:%S")
        print("Login successful...")
        welcome()

        full_name = database[accountNumberFromUser]["first_name"] + " " + database[accountNumberFromUser]["last_name"]
        print(f"{full_name}, You logged in at: {dt_string}")

        bankOperations(accountNumberFromUser)
    else:
        print("Invalid account Number or Password")
        print("Looks like you do not have an account with us, would you like to register ?\n")
        register_or_login = input("Press (1) to register or (2) to go back to login page\n")

        try:
            register_or_login = int(register_or_login)
        except:
            pass
        
        if register_or_login == 1:
            register()
        else:
            print("""
            ++++++++++++++++++++++++++++++++++
                provide your Login details
            ++++++++++++++++++++++++++++++++++
                """)
            login()



# A simple function to Register new accounts, this would also add the generated account to the local database
def register():
    print("""
    ********** Regsiteration page **********
    Kindly provide your details to complete your registeration.
    """)

    email = input("Type in your email adress: ")
    first_name = input("\nWhats your First name ?: ")
    last_name = input("\nWhats your Last name ?: ")
    password = input("\nChoose a password: ")
    balance = int(input("How much would you like to deposit ?: "))
    account_number = generateAccountNumber()

    #This action would simply add all the details of the person to the local database
    database[account_number] = {"email": email, "first_name" : first_name, "last_name": last_name, "password": password, "balance": balance}

    # print(database)
    print(f"""\nCongrats, you have successfully registered and your account has been created.
    ================================================================
        Your account Number is {account_number}.
        Please copy it and keep it somewhere safe. Thank you !
    ================================================================
    *******Redirecting to login page...******""")
    input("Hit enter to clear the screen and proceed to Login page, kindly make sure you already copied your account number.... ")
    system("cls")
    login()


# A simple function to generate an account number
def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


# A function to perform certain operations based on users input.
def bankOperations(accountNumberFromUser):
    optionSelected = input("""
What would you like to do ?
    (1.) Deposit
    (2.) Withdrawal
    (3.) Check account Balance
    (4.) Logout
    (5.) Register a complaint
    (6.) Exit
    \n""")

    try:
        optionSelected = int(optionSelected)
    except:
        pass

    if optionSelected == 1:
        deposit = int(input("How much would you like to deposit ?: "))
        depositOperation(accountNumberFromUser, deposit)

    elif optionSelected == 2:
        witdrawCash = int(input("How much would you like to withdraw ?: "))
        withdrawalOperation(accountNumberFromUser, witdrawCash)

    elif optionSelected == 3:
        check_balance(accountNumberFromUser)

    elif optionSelected == 4:
        print("Successfully logged out....")
        LogoutOption()

    elif optionSelected == 5:
        complains = input("What issue would you like to report ?\n")
        complaint(accountNumberFromUser, complains)
        
    elif optionSelected == 6:
        print("Thank you for banking with us... ")
        exit()

    else:
        print("Invalid Option, please Try again")
        bankOperations(accountNumberFromUser)


# When a user opts to log out, he is presnted with these options to choose from
def LogoutOption():
    optionToLogOut = input("""
Choose one (1) option please. Press,
    (1) to proceed to Login page
    (2) to create a new account
    (3) to exit
        \n""")
    try:
        optionToLogOut = int(optionToLogOut)
    except:
        pass

    if optionToLogOut == 1:
        print("""
            *************************************
            Redirecting you to the Login page...
            *************************************
            """)
        login()

    elif optionToLogOut == 2:
        print("""
            *********************************************
            Redirecting you to the Registeration page...
            *********************************************
            """)
        register()

    elif optionToLogOut == 3:
        print("Thank you for banking with us...")
        exit()

    else:
        print("You selected an invalid option")
        print("These are the available options, please select one\n")
        LogoutOption()


# A function to update the user details to the local database.
def updateInfo(accountNumberFromUser, info_to_update, value_for_update):
    database[accountNumberFromUser].update({info_to_update : value_for_update})


def check_balance(accountNumberFromUser):
    current_balance = database[accountNumberFromUser]["balance"]
    print(f"Your current balance is {current_balance}")
    bankOperations(accountNumberFromUser)


# A function to withdraw some amount of money from a users account and update his current balance.
# To witdraw, account balance must be greater than zero (0)
def withdrawalOperation(accountNumberFromUser, witdrawCash):
    current_balance = database[accountNumberFromUser]["balance"]

    #Checks if amount to withdraw is less than the current account balance
    if witdrawCash < current_balance:
        current_balance -= witdrawCash
        print(f"You successfully withdrew {witdrawCash}")
        print(f"Your current account balance is {current_balance}")

        updateInfo(accountNumberFromUser, "balance", current_balance)        
        print("Thank you !")
        bankOperations(accountNumberFromUser)
    else:
        print("You have insufficient Balance")
        bankOperations(accountNumberFromUser)


def depositOperation(accountNumberFromUser ,deposit):
    current_balance = database[accountNumberFromUser]["balance"]
    current_balance += deposit
    print(f"You successfully deposited {deposit}")
    print(f"Your current account balance is {current_balance}")

    updateInfo(accountNumberFromUser, "balance", current_balance)    
    print("Thank you !")

    bankOperations(accountNumberFromUser)


def complaint(accountNumberFromUser, complains):
    updateInfo(accountNumberFromUser, "complaint", complains)
    print("Your complaint has been recieved and you would recieve a feedback from us within 24 hours")
    print("Thank you for Banking with us.")
    bankOperations(accountNumberFromUser)



def initialize():
    welcome()
    print("Do you have an account with us ? \n")
    have_account = input("1. (Yes)\n2. (No)\n")

    try:
         have_account = int(have_account)
    except:
        pass
    
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You entered an incorrect option, please try again.\n")
        input("Hit enter to Continue ... ")
        system('cls')
        initialize()


initialize() 