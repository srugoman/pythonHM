#python cannot do recursion over 997
decorator = [None]*997


def factorial(num):
    if num == 1:
        return 1
    if decorator[num]:
        print("decorator used")
        return decorator[num]
    fact = num * factorial(num-1)
    decorator[num] = fact
    return fact


def main():
    print(factorial(25))
    print(factorial(30))



if __name__ == '__main__':
    main()

