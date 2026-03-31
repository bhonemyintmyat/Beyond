nums = [23,24,25,4,5,1]

c = []
total = 0
previous_num = 0
for i in range(len(nums)):
    if i+1 != len(nums):
        if nums[i] != previous_num:
            if nums[i+1] == nums[i] + 1 or nums[i]-1 == nums[i-1]:
                    c.append(nums[i])
                    previous_num = nums[i]
        else:
            break
    else:
        if nums[i]-1 == nums[i-1]:
            c.append(nums[i])
         

total = 0
for i in c:
    total +=i
while total in nums: 
    total+=1
print(total)