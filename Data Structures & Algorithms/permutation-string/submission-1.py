class Solution:
    def helper(self,a,b):
        hash_list = [0]*26
        for i in a:
            hash_list[ord(i)-ord('a')]+=1
        for i in b:
            hash_list[ord(i)-ord('a')]-=1
        if hash_list == [0]*26:
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
            
            


        