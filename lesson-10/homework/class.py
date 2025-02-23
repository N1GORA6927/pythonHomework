
class Account:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        
    def get_balance(self):
        print(self.balance)
    def deposit_money(self,deposit_amount):
        self.balance += deposit_amount
        return self.balance
    def withdraw_money(self,withdraw_amount):
        if self.balance > withdraw_amount:
            self.balance -= withdraw_amount
            return True
        else:
            return False
    def __str__(self):
        return f'Account Number {self.account_number}\nHolder Name {self.holder_name}\nBalance {self.balance}'
    
    
class Bank:
    account_list = []
    def __init__(self,bank_name):
        self.bank_name = bank_name
    def add_account(self,account_number):
        if len(self.account_list) < 1:
            holder_name = input('Enter Holder Name ')
            account_object = Account(account_number,holder_name)
            self.account_list.append(account_object)
            
        else:
            for i in self.account_list:
                if i.account_number != account_number:
                    holder_name = input('Enter Holder Name ')
                    account_object = Account(account_number,holder_name)
                    self.account_list.append(account_object)
                    print(f'AccountNumber {account_object.account_number} was added successfully!')
                    break
                else:
                    print(f'Account Number {i.account_number} is already exists')
    def list_all_accounts(self):
        for i in self.account_list:
            print( f'{i.account_number} -- {i.balance}')
    def check_balance(self,account_number):
        for i in self.account_list:
            if i.account_number == account_number:
                i.get_balance()
            else:
                print(f'Account Number {i.account_number} does not exist')
    def get_money(self,account_number):
        for i in self.account_list:
            if i.account_number == account_number:
                withdraw_amount = int(input('Enter withdraw amount '))
                if i.withdraw_money(withdraw_amount):
                    print(f'Process is completed successfully\nCurrent balance: {i.balance}')
                else:
                    print(f'{i.balance} is not enough to withdraw {withdraw_amount}')
            else:
                print(f'Account Number {account_number} does not exist')
    def deposit_money(self,account_number):
        for i in self.account_list:
            if i.account_number == account_number:
                deposit_amount = int(input('Enter depsoit amount '))
                i.deposit_money(deposit_amount)
                print(f'Account Number: {i.account_number} Current Balance: {i.balance}')
            else:
                print(f'Account Number {account_number} does not exist')
                    
def print_menu():
    print("\nBank Account Management Menu:")
    print("1. Add an account")
    print("2. List all accounts")
    print("3. deposit money")
    print("4. withdraw money")
    print("5. Account details")
    print("5. Exit")


    
def main():
    Central_bank = Bank('MB')
    while True:
        choice = input('please select numbers: ')
        if choice == '1':
            account_number = int(input('Enter Account Number '))
            
            Central_bank.add_account(account_number)
        elif choice == '2':
            Central_bank.list_all_accounts()
        elif choice == '3':
            account_number = int(input('Enter Account Number '))
            Central_bank.deposit_money(account_number)
        elif choice == '4':
            account_number = int(input('Enter Account Number '))
            Central_bank.get_money(account_number)
        elif choice == '5':
            account_number = int(input('Enter Account Number '))
            Central_bank.check_balance(account_number)
            
            
            
        else:
            break
            
a = print_menu()
b = main()
