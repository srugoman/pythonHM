
def getcode(code):
    enteredcode = int(input("please enter the seceret code:"))
    print(enteredcode)
    while enteredcode != code:
        enteredcode = int(input("wrong code,please try again:"))


def printbalance(balance):
    print("your current balance is:", balance)


def cashwithdraw(balance):
    amount = int(input("how much money do you want to withdraw "))
    balance -= amount
    return balance


def changecode(newcode):
    code = newcode


def main():
    code = int(1234)
    balance = int(1000)
    getcode(code)
    balance = cashwithdraw(balance)


if __name__ == '__main__':
    main()



