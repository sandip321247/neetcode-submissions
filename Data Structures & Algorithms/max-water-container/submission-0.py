class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        area = 0
        while l < len(heights):
            for r in range(1 , len(heights)):
                h =min(heights[l] , heights[r])
                b = r - l
                area = max(area , h*b)
            l += 1
        return area

