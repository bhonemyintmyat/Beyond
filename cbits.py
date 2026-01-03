n = int(input("Enter: "))

c = []
res = 0
remainder = 0
for i in range(0,n+1):
    if i == 0:
        c.append(0)
    elif i > 0:
        while i / 2 != 0:
            remainder = i % 2
            i = i // 2
            res = res + remainder
        if i / 2 == 0:
            c.append(res)
            res = 0
        
        
print(c)