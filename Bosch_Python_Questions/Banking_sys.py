from datetime import datetime, timedelta

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - Holder: {self.account_holder}, Balance: Rs.{self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest Rs.{interest:.2f}. New balance: Rs.{self.balance:.2f}")

    def __str__(self):
        return super().__str__() + f", Savings Account with interest rate: {self.interest_rate * 100:.2f}%"


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal amount exceeds overdraft limit.")
        self.balance -= amount
        print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")

    def __str__(self):
        return super().__str__() + f", Current Account with overdraft limit: Rs.{self.overdraft_limit:.2f}"

class FixedDepositAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, lock_in_period_months=12, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.lock_in_period = timedelta(days=lock_in_period_months * 5)
        self.interest_rate = interest_rate
        self.start_date = datetime.now()

    def withdraw(self, amount):
        if datetime.now() < self.start_date + self.lock_in_period:
            raise ValueError("Cannot withdraw during lock-in period.")
        super().withdraw(amount)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied fixed deposit interest Rs.{interest:.2f}. New balance: Rs.{self.balance:.2f}")

    def __str__(self):
        lock_in_end = self.start_date + self.lock_in_period
        return (super().__str__() +
                f", Fixed Deposit Account with interest rate: {self.interest_rate * 100:.2f}%, "
                f"lock-in ends on {lock_in_end.strftime('%Y-%m-%d')}")
    
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added.")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]

    def transfer_funds(self, from_acc_num, to_acc_num, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        from_acc = self.get_account(from_acc_num)
        to_acc = self.get_account(to_acc_num)

        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"Transferred Rs.{amount:.2f} from {from_acc_num} to {to_acc_num}.")

def main():
    bank = Bank()

    savings = SavingsAccount("1001", "Nagaraju", 1000.0)
    current = CurrentAccount("1002", "Kumar", 500.0, overdraft_limit=300.0)
    fixed_deposit = FixedDepositAccount("1003", "Gupta", 2000.0, lock_in_period_months=6)

    bank.add_account(savings)
    bank.add_account(current)
    bank.add_account(fixed_deposit)

    print("\n--- Initial Account Details ---")
    print(savings)
    print(current)
    print(fixed_deposit)

    print("\n")
    savings.deposit(500)
    current.deposit(200)
    fixed_deposit.deposit(500)

    print("\n")
    try:
        savings.withdraw(300)
    except ValueError as e:
        print(e)

    try:
        current.withdraw(700) 
    except ValueError as e:
        print(e)

    try:
        fixed_deposit.withdraw(100) 
    except ValueError as e:
        print(e)

    print("\n")
    savings.apply_interest()
    fixed_deposit.apply_interest()

    print("\n")
    try:
        bank.transfer_funds("1001", "1002", 200)
    except ValueError as e:
        print(e)

    print("\n--- Final Account Details ---")
    print(savings)
    print(current)
    print(fixed_deposit)

if __name__ == "__main__":
    main()
