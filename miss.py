nums = [1]
n = len(nums)
gauss = n*(n+1)//2
add = 0
for i in nums:
    add = add + i
diff = gauss - add
if diff == 0:
    print(diff)
        