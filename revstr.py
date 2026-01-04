def main():
    s = list(input("Input a string: "))
    print(rev(s))
def rev(s):
    for i in range(len(s)//2):
        temp = s[i]
        s[i] = s[-1-i]
        s[-1-i] = temp
    return(s)

main()