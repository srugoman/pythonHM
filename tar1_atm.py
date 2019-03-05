code = int(1234)
balance = int(1000)


def getcode():
    enteredcode = int(input("please enter the seceret code:"))
    print(enteredcode)
    while enteredcode != code:
        enteredcode = int(input("wrong code,please try again:"))


def printbalance():
    print("your current balance is:", balance)


def cashwithdraw(curbalance):
    amount = int(input("how much money do you want to withdraw "))
    curbalance -= amount
    return curbalance


def main():
    getcode()
    cashwithdraw()


if __name__ == '__main__':
    main()



