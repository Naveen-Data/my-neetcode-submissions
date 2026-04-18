class Solution:
    def helper(self,a,b):
        r1 = ''.join(sorted(a))
        r2 = ''.join(sorted(b))
        if r1 == r2:
            return True
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        
        while l < r:
            if len(s2[l:r]) < len(s1):
                print(s2[l:r])
                return False
            if self.helper(s1,s2[l:r]):
                return True
            else:
                l+=1
                r+=1
            
            


        