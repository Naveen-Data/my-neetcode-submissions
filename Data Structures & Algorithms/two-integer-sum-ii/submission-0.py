class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for key, num in enumerate(numbers):
            hash_map[num] = key

        for i in range( len(numbers)):
            required = target - numbers[i]
            if required in hash_map:
                return [ i + 1, hash_map[required]+1]


            
        