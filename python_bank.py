#Created by Akshay Bhat id @zicron13


class Bank:
    def __init__(self, name=None):
        self.name = name
        self.ac_no = None  # Initialize account number to None
        self.details = []  # Initialize details as an empty list

    def create_account(self):
        self.name = input('Enter your name: ')
        import random
        self.ac_no = random.randint(1000000000, 9999999999)
        self.details = [self.name, self.ac_no, 0.0]  # Initialize details with balance
        print(f'Account created for {self.name} with account number: {self.ac_no}')

    def display_details(self):
        if self.name is None or self.ac_no is None:
            print("No account created yet.")
        else:
            print(self.details)  # Return the list with details

    def deposit(self):
        self.amount = float(input('Enter the amount to be deposited: '))
        self.details[2] += self.amount  # Update balance in details
        return self.details

    def withdraw(self):
        self.withdr = float(input('Enter amount to be withdrawn: '))
        if self.withdr > self.details[2]:
            print('You have insufficient balance')
        else:
            self.details[2] -= self.withdr  # Update balance in details
        print(f'Your balance is {self.details[2]}')
        return self.details

    def delete_acc(self):
        d = input('You want to delete your account? Y/N: ')
        if d.upper() == 'Y':
            self.details.clear()  # Clear details
            self.name = None
            self.ac_no = None
            print('Your account and the data from the database have been removed successfully!')
            print('Happy Banking !!!')
        else:
            print(f'Your account details: {self.details}')

def main():
    B = Bank() 
    print('Welcome to Python Bank!!!')
    status = True
    while status:
        option = input('Select options: Create account : C  , Display details : D , Deposit : DEP , Withdraw : W , Delete account : DEL , Quit : Q: ')
        
        match option:
            case 'C':
                B.create_account()
            case 'D':
                B.display_details()
            case 'DEP':
                B.deposit()
            case 'W':
                B.withdraw()
            case 'DEL':
                B.delete_acc()
            case 'Q':
                print('Thank you for using Python Bank! Exiting...')
                status = False  # Set status to False to break the loop and exit
            case _:
                print('Invalid option. Please try again.')



main()
 # Print the list containing the account holder's name and account number
