class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_check_set = set()
        for i in nums:
            if i in duplicate_check_set:
                return True
            duplicate_check_set.add(i)
        return False