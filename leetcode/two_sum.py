class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for count, ele in enumerate(nums):
            diff = target - ele
            if diff in hashmap:
                return [hashmap[diff], count]
            hashmap[ele] = count
        return