words = ["Alaska","Dad"]
c = []
first = "qwertyuiop"
second = "asdfghjkl"
third = "zxcvbnm"
for word in words:
    word = word.lower()
    if word[0] in first:
        for i in word:
            if i in first:
                if i != len(word):
                    continue
                else:
                    c.append(word)
    if word[0] in second:
        for i in enumerate(word):
            if i in second:
                if word.index(i) != len(word) - 1:
                    continue
                else:
                    c.append(word)
    if word[0] in third:
        for i in word:
            if i in third:
                if i != len(word):
                    continue
                else:
                    c.append(word)
print(c)
    
                
