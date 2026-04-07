class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        
        
        max_seen_so_far = 0
        for i in hash_set:
            if i-1 not in hash_set:
                count = 1
                current = i
                while current+1 in hash_set:
                    count+=1
                    current +=1
                max_seen_so_far = max(count,max_seen_so_far)

        return max_seen_so_far
        
    
                
    
        