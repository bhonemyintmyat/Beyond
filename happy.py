def main():
    n = int(input("Enter num: "))
    print(happy(n))

def happy(n):
    c = []
    a = 0
    while n != 1 and n != 4:
        while n > 0:
            digit = n % 10
            c.append(digit)
            n //= 10

        for i in c:
            num = i**2
            a = a+num
        n = a
        a = 0
        c = []
    if n == 1:
        return True
    elif n == 4:
        return False
    happy(n)

if __name__ == "__main__":
    main()
    