nums = [1,2,3,2,5]
length = len(nums) - 1
for i in range(length):
    current_sum = nums[i]
    next_number = nums[i+1]
    if nums[i]+1 == nums[i+1]:
        current_sum = current_sum + next_number
while current_sum in nums: 
    current_sum+=1
print(current_sum)