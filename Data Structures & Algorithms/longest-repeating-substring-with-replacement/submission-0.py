class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freq_count_hashmap = {}
        maxf = 0
        res = 0
        while r < len(s):
            if s[r] not in freq_count_hashmap:
                freq_count_hashmap[s[r]] = 1
            else:
                freq_count_hashmap[s[r]] += 1
            maxf = max(maxf,freq_count_hashmap[s[r]])
            while ((r-l+1) - maxf > k ):
                freq_count_hashmap[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
            r+=1
        return res
        


