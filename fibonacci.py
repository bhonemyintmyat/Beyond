def main():
    n = int(input("Enter: "))
    print(fibonacci(n))
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        a = 0
        b = 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b







if __name__ == "__main__":
    main()