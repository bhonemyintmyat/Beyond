operations = ["5","2","C","D","+"]
c = []
for i in operations:
    if i != 'C' and i != "D" and i != "+":
        c.append(int(i))
    elif i == "C":
        c.pop()
    elif i == "D":
        c.append(2*c[-1])
    elif i == "+":
        c.append(c[-2]+c[-1])
print(sum(c))