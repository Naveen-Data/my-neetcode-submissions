class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left < right:
            required = target - numbers[left]
            if required < numbers[right]:
                right-=1
            elif required > numbers[right]:
                left+=1
            else:
                return [ left+1, right+1]