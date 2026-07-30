class Solution:
    def trap(self, height: List[int]) -> int:
        # rain trapped in curr pos = min(maxL, maxR) - currentHeight
        # maxL and maxR start at 0
        # they are the max height seen anywhere on the left/right of curr pos
        # use 2 pointers:
        # 1. start at each end of array
        # 2. calc rain trapped at curr pos
        # 3. update maxL or maxR
        # 4. move pointer that has lowest val (if both equal then just move left - doesnt matter)

        totalRain = 0
        maxL = height[0]
        maxR = height[-1]

        idxL = 0
        idxR = len(height)-1

        lastUpdatedWasLeft = True

        while idxL <= idxR:
            currHeight = height[idxL] if lastUpdatedWasLeft else height[idxR]

            # calc rain
            rain = min(maxL, maxR) - currHeight

            # update total rain
            if rain > 0:
                totalRain += rain
            
            # update maxL and maxR
            maxL = max(maxL, height[idxL])
            maxR = max(maxR, height[idxR])

            # move pointer
            if maxL <= maxR:
                # move left
                idxL += 1
                lastUpdatedWasLeft = True
            else:
                # move right
                idxR -= 1
                lastUpdatedWasLeft = False
        
        return totalRain
