words= ["adsdf","sfd"]
c = []
first = "QWERTYUIOPqwertyuiop"
second = "ASDFGHJKLasdfghjkl"
third = "ZXCVBNMzxcvbnm"
for word in words:
    if word[0] in first:
        for i in range(len(word)):
            if word[i] in first:
                if i != len(word)-1:
                    continue
                else:
                    c.append(word)
            else:
                break
    if word[0] in second:
        for i in range(len(word)):
            if word[i] in second:
                if i != len(word)-1:
                    continue
                else:
                    c.append(word)
            else:
                break
    if word[0] in third:
        for i in range(len(word)):
            if word[i] in third:
                if i != len(word)-1:
                    continue
                else:
                    c.append(word)
        else:
            break
print(c)