def sumuntilstop():
    sumerize = 0
    uinput = input("please enter number:")
    while uinput != "stop":
        sumerize += int(uinput)
        uinput = input("please enter number:")
    print("sum is:",sumerize)


def main():
    sumuntilstop()


if __name__ == "__main__":
    main()

