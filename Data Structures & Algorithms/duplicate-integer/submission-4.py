class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap = {}
        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i]+=1
        #         return True
        #     hashmap[i]=1
        # return False
        

        # if len(nums) != len(set(nums)):
        #     return True 
        # return False

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


