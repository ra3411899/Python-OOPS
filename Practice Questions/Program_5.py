# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
class BankAccount:
# Create a constructor with parameters: accountNumber, name, balance.
    def __init__(self, accountNumber : int, name : str, balance : float):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        return 'Account Details\nAccount Number : {}\tName : {}\tBalance : {:.2f}'.format(self.accountNumber, self.name, self.balance)

# Create a Deposit() method which manages the deposit actions.
    def Deposit(self, depositAmount : float):
        self.balance += depositAmount
        print('Deposited Sucessfully, Your Current Balance is : {:.2f}'.format(self.balance))
# Create a Withdrawal() method  which manages withdrawals actions.
    def Withdrawal(self, withdrawlAmount):
        self.balance -= withdrawlAmount
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
    def bankFees(self):
        return self.balance - (self.balance * 0.05)
# Create a display() method to display account details.
    def display(self):
        return '\nAccount Details\nAccount Number : {}\tName : {}\tBalance : {:.2f}'.format(self.accountNumber, self.name, self.balance)
# Give the complete code for the  BankAccount class.

if __name__ == '__main__':
    bankAccountObject = BankAccount(3112456, 'Riyaz Ali', 9087.89)
    print(bankAccountObject.display())
    bankAccountObject.Deposit(1000.9999)
    print(bankAccountObject.display())