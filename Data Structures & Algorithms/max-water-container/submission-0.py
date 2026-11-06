class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights) - 1

        max_area = 0

        while lo < hi:
           width = hi - lo
           height = min(heights[lo], heights[hi])
           max_area  = max(max_area, height * width)

           if heights[lo] < heights[hi]:
              lo += 1
           else:
              hi -= 1

        return max_area


