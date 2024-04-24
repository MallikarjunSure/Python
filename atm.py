class ATM:
    def __init__(self, initial_balance=50):
        self.balance = initial_balance
        self.transaction_count = 0
        self.transaction_limit = 5
        self.minimum_balance = 50
    
    def check_balance(self):
        if self.transaction_count < self.transaction_limit:
            self.transaction_count += 1
            print(f"Current Balance: ${self.balance:.2f}")
        else:
            print("Transaction limit reached.")
    
    def deposit(self, amount):
        if self.transaction_count < self.transaction_limit:
            if amount > 0:
                self.balance += amount
                self.transaction_count += 1
                print(f"Deposited: ${amount:.2f}")
                print(f"New Balance: ${self.balance:.2f}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Transaction limit reached.")
    
    def withdraw(self, amount):
        if self.transaction_count < self.transaction_limit:
            if amount <= 0:
                print("Invalid amount to withdraw.")
            elif amount > self.balance - self.minimum_balance:
                print("Insufficient funds to maintain minimum balance.")
            else:
                self.balance -= amount
                self.transaction_count += 1
                print(f"Withdrew: ${amount:.2f}")
                print(f"Remaining Balance: ${self.balance:.2f}")
        else:
            print("Transaction limit reached.")
    
    def reset_transactions(self):
        self.transaction_count = 0
        print("Transaction count has been reset.")

def main():
    print("Welcome to the ATM")
    my_atm = ATM(100)  # starting with an example balance

    while True:
        print("\nChoose an action:")
        print("1: Check Balance")
        print("2: Deposit Money")
        print("3: Withdraw Money")
        print("4: Reset Transaction Count")
        print("5: Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            my_atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            my_atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            my_atm.withdraw(amount)
        elif choice == '4':
            my_atm.reset_transactions()
        elif choice == '5':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid choice, please choose from 1-5.")

if __name__ == "__main__":
    main()
