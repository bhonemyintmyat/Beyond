s = "PPALLP"
absent = 0
late = 0
present = 0
for i in s:
    if i == "A":
        absent += 1
        if absent >= 2:
            print("False")
    if i == "L":
        late +=1
        if late >= 3:
            print("False")
    else:
        late = 0
print(True)