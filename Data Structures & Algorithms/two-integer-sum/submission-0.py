class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0,len(nums)):
            seen = target - nums[i]
            if seen in hashmap:
                return [hashmap[seen],i]
           
            hashmap[nums[i]] = i
        
        