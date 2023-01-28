nums = [1,3,5,6]
target = 7
count =0
for i in range(len(nums)):
    if nums[i] < target:
        count+=1
    if nums[i]==target:
        count = i
print(count)