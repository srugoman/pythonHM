decorator = []


def factorial(num):
    if num == 1:
        return 1
    fact = num + factorial(num-1)
    return fact

def main():
    print("main")



if __name__ == '__main__':
    main()

