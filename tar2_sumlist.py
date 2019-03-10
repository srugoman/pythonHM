def sumuntilstop():
    sumerize = 0
    uinput = input("please enter number:")
    while uinput != "stop":
        sumerize += int(uinput)
        uinput = input("please enter number:")
    print("sum is:",sumerize)
def sumfromstring():
    sum = 0
    uinput = input("enter list of numbers")
    for i in uinput:
        if i != ',':
            sum += int(i)
    print(sum)


def main():
    sumuntilstop()
    sumfromstring()

if __name__ == "__main__":
    main()

