def square(x):
    return x * x


def Map(f,list):
    newlist = []
    for x in list:
        newlist.append(f(x))
    return newlist


def main():
    list = [1,2,3]
    print(list)
    list = Map(square,list)
    print(list)


if __name__ == '__main__':
    main()

