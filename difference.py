s = list("a")
t = list("aa")

c = []
try:
    for i in range(len(t)):
        if t[i] == s[i]:
            continue
        else:
            c.append(t[i])
except IndexError:
    print(t[i])

