code = 1234
balance = 1000


def getcode():
    enteredcode = int(input("please enter the seceret code:"))
    print(enteredcode)
    while enteredcode != code:
        enteredcode = int(input("wrong code,please try again:"))


def printbalance():
    print("your current balance is:", balance)


def main():
    getcode()


if __name__ == '__main__':
    main()



