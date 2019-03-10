import sys
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


def changecode():
    return int(input("enter new secret code:"))


def exit():
    sys.exit()


def main():
    code = int(1234)
    balance = int(1000)
    uinput = 0
    while uinput != 4:
        getcode(code)
        uinput = int(input("enter 1 to print you balance, 2 for cash withdrawal, 3 to change your code or 4 to exit "))
        if uinput == 1:
            printbalance(balance)
        else:
            if uinput == 2:
                balance = cashwithdraw(balance)
            else:
                if uinput == 3:
                    code = changecode()
                else:
                    if uinput == 4:
                        exit()
                    else:
                        print("wrong inout, start over")









if __name__ == '__main__':
    main()



