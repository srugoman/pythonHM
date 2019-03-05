code = 1234
amount = 1000


def getcode():
    entered = int(input("please enter the seceret code:"))
    print(entered)
    while entered != code:
        entered = int(input("wrong code,please try again:"))


def main():
    getcode()


if __name__ == '__main__':
    main()



