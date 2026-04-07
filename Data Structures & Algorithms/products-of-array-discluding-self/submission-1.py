class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        multiply = 1
        for i in range(len(nums)):
            res[i]= multiply
            multiply *= nums[i]

        multiply = 1
        for j in range((len(nums)-1),-1,-1):
            res[j]= multiply * res[j]
            multiply *= nums[j]

        return res
