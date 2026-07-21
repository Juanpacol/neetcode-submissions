class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l=0
        r=len(heights)-1
        max_water=0

        while l < r:
            width=r-l 
            currentheight=min(heights[l], heights[r])
            currentwater= width * currentheight
            max_water=max(max_water, currentwater)

            if heights[l] < heights[r]:
                l += 1 
            else:
                r -=1
        return max_water


