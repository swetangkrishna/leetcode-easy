

nums = [0,0,0,1,1,1,1,2,2]
count =1
val =nums[0]
for i in range(len(nums)):
    if nums[i]!= val:
        nums[count]=nums[i]
        val = nums[i]
        count+=1

        
print(count)
print(nums)
