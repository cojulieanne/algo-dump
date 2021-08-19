class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            comp = target - nums[i]
            if(comp in nums[i+1:]):
                return([i, nums[i+1:].index(comp)+i+1])
                break
