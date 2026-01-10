pattern = list("abba")
s = "dog dog dog dog".split(" ")
my_dict = {}
for i in range(len(pattern)):
    if pattern[i]  not in my_dict:
        my_dict[pattern[i]] = s[i]
    else:
        continue

for i in range(len(s)):
    temp = s[i]
    if temp in my_dict.values():
        continue
    else:
        print("False")
        break
if temp in my_dict.values():
    print("True")


