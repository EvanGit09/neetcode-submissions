class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bottomIdx = 0
        topIdx = len(heights)-1
        currentLength = len(heights)-1

        # idea start at both ends and then slowly move the side that has the lower value in and recalculate the area
        maxArea = 0
        while bottomIdx < topIdx:
            # get heights
            top = heights[topIdx]
            bottom = heights[bottomIdx]
            # calc area
            currArea = min(top, bottom) * currentLength
            # update max
            maxArea = max(maxArea, currArea)

            # move lowest
            if top < bottom:
                topIdx -= 1
            else:
                bottomIdx += 1
            
            # update length
            currentLength -= 1
        
        return maxArea
