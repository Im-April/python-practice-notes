class BankAcount :
    def __init__(self, owner,balance=0) :
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount}원 입금. 잔액 : {self.balance}원')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('잔액이 부족합니다.')
        else :
            self.balance -= amount
            print(f'{amount}원 출금. 잔액 : {self.balance}원')


my_account = BankAcount('홍길동',10000)
my_account.deposit(5000) # 5000원 입금
my_account.withdraw(3000) # 3000원 출금