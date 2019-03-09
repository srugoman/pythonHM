
def stringShrinker(str):
    newStr = []
    index1 = 0

    while index1 < len(str):
        index2 = index1
        count = 0
        while index2 < len(str):
            if str[index2] == str[index1]:
                count += 1
            else:
                break
            index2 += 1
        newStr += [str[index1]]+[count]
        index1 = index2
    return newStr




def main():
    str = 'abbcccdddd'
    print("main\n")
    print(stringShrinker(str))



if __name__ == "__main__":
    main()

