left = int(input("Enter: "))
right = int(input("Enter: "))
c = []
for i in range(left, right+1):
    digits_list = [int(digit) for digit in str(i)]
    if i < 10:
        c.append(i)
    else: 
        if all(a != 0 and i % a == 0 for a in digits_list):
            c.append(i)
print(c)
            
