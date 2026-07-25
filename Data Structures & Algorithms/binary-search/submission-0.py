class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initial checks
        if len(nums) <= 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        bottomIdx = 0
        topIdx = len(nums)-1
        while bottomIdx <= topIdx:
            if bottomIdx == topIdx:
                if nums[bottomIdx] == target:
                    return bottomIdx
                else:
                    return -1
            midIdx = bottomIdx + round((topIdx-bottomIdx)/2)
            mid = nums[midIdx]
            if mid == target:
                return midIdx
            elif mid > target:
                # set top to below mid
                topIdx = midIdx-1
            else:
                # set bottom to above mid
                bottomIdx = midIdx+1
        
        return -1