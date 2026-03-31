def main():
    n = int(input("Enter n: "))
    print(climb(n))
def climb(n):
    if n <= 3: 
        return(n)
    a = (1, 2)
    for i in range(3, n+1):
        a = (a[1], a[0]+a[1])
    return(a[-1])

if __name__ == "__main__":
    main()


            
        