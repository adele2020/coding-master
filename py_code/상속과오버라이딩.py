#### 상속과 오버라이딩 ####
# 계좌 class 생성
class Account :
    accountName = ""
    balance = 0

    def __init__(self, name, balance):
        self.accountName = name
        self.balance = balance

    def deposit(self, money):
        print("%s 계좌의 입금액은 %d 입니다." %(self.accountName, money))
        self.balance += money
        print("%s 계좌의 현재 잔액은 %d 입니다." %(self.accountName, self.balance))

    def withdrawal(self, money):
        if self.balance < money:
            print("현재 잔액보다 출금액이 큽니다")
        else:
            print("%s 계좌의 출금액은 %d 입니다." %(self.accountName, money))
            self.balance -= money
            print("%s 계좌의 현재 잔액은 %d 입니다." %(self.accountName, self.balance))


# 기본계좌
class AccountBasic(Account):
    pass

# 입금시 이자가 20%인 계좌
class AccountInterest20(Account):
    interest = 0

    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.interest = 0.2

    def deposit(self, money):
        print("%s 계좌의 입금액은 %d 입니다." %(self.accountName, money))
        self.balance += money
        self.balance += (self.balance * self.interest)
        print("%s 계좌의 현재 잔액은 %d 입니다." %(self.accountName, self.balance))

# 입금시 이자가 10%인 계좌
class AccountInterest10(Account):
    interest = 0

    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.interest = 0.1

    def deposit(self, money):
        print("%s 계좌의 입금액은 %d 입니다." %(self.accountName, money))
        self.balance += money
        self.balance += (self.balance * self.interest)
        print("%s 계좌의 현재 잔액은 %d 입니다." %(self.accountName, self.balance))

# 변수 선언 부분
myAcnt1, myAcnt2, myAcnt3 = None, None, None

# 메인 코드 부분
myAcnt1 = AccountBasic("기본",100000)
myAcnt2 = AccountInterest20("이자가20퍼센트",100000)
myAcnt3 = AccountInterest10("이자가10퍼센트",100000)

print("------------------------<입금>-----------------------------------")

myAcnt1.deposit(10000)
myAcnt2.deposit(10000)
myAcnt3.deposit(10000)

print("-------------------------<출금>----------------------------------")

myAcnt1.withdrawal(110000)
myAcnt2.withdrawal(110000)
myAcnt3.withdrawal(110000)
