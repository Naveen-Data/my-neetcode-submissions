class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        
        count = 0
        max_seen_so_far = 0
        for i in nums:
            if i-1 not in hash_set:
                count = 1
                if count > max_seen_so_far:
                        max_seen_so_far = count
                while i+1 in hash_set:
                    count+=1
                    if count > max_seen_so_far:
                        max_seen_so_far = count
                    i+=1
        return max_seen_so_far
        
    
                
    
            
                
                
                
            


        return count
        