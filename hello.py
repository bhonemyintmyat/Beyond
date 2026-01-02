def main():
    n=int(input("What's the number? "))
    print("Factorial is", factorial(n))
    print("Hello, World")
    n = 5
    for i in range(0,n):
        print(i)

    while n != 0:
        print("hi")
        n -=1
def factorial(n):
    if n<=1:
        return 1
    ans = 1
    while n>0:
        ans = ans * n
        n=n-1
    return ans

main()





