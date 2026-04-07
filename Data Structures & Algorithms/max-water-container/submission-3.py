class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = -1
        while i < j:
            if heights[i] < heights[j]:
                area = min(heights[i],heights[j])*(j-i)
                if area > max_area:
                    max_area = area
                i += 1
                
            else:
                area = min(heights[i],heights[j])*(j-i)
                if area > max_area:
                    max_area = area
                j-=1
                
        return max_area