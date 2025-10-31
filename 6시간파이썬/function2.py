def deposit(balance, money) : # 입금 함수
    print(f'입금이 완료되었습니다.\n잔액은 {balance + money}원 입니다.')
    return balance + money

def withdraw(balance, money) : # 출금 함수
    if balance >= money :
        print(f'출금이 완료되었습니다.\n잔액은 {balance-money}원 입니다.')
        return balance - money
    else :
        print('잔액이 부족합니다.')
    
    return balance

def withdraw_night(balance, money) :
    commision = 100 # 수수료
    return commision, balance-money-commision

balance = 0
balance = deposit(balance, 1000)
print(balance)
commision, balance = withdraw_night(balance,500)
print(f'수수료는 {commision}원 이며 잔액은 {balance}원 입니다.')