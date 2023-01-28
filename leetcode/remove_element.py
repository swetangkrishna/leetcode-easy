def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count =0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count +=1
            else:
                nums.remove(val)
                nums.append("_")
        
        print(count-1)
        print(nums)    


num_var = [0,1,2,2,3,0,4,2]
key = 2
removeElement(num_var,key)