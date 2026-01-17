s = ""
t = "a"

c = []
for i in range(len(t)):
    if i < len(s):
        chai = ord(s[i])
        chat = ord(t[i])
        if chat - chai == 0:
            continue
        else:
            c.append(t[i])
    else:
        if t[i] in s and t[i] in c:
            break
        else:
            c.append(t[i])
print(c[0])
    