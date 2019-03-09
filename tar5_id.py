
def checkid(id):
    if len(id) != 9:
        return False
    index = 0
    count = 0
    while index < len(id)-1:
        temp = str(int(id[index]) * (2 - ((index + 1) % 2))) + '0'
        count += int(temp[1]) + int(temp[0])
        index += 1
    num = 0
    if count % 10 != 0:
        num = 10 - (count % 10)

    if int(id[len(id)-1]) != num:
        return False
    return True


def main():
    print("main\n")
    id = "543700421"
    print(checkid(id))


if __name__ == '__main__':
    main()


