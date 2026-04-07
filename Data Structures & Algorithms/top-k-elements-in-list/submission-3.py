
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        
        
        res = []
        for key,value in hashmap.items():
            if len(res) < k :
                res.append(key)
            else:
                smallest = res[0]
                for i in range(1,len(res)):
                    if hashmap[res[i]] < hashmap[smallest]:
                        smallest = res[i]
                if value > hashmap[smallest]:
                    res.append(key)
                    res.remove(smallest)
        return res
                
        