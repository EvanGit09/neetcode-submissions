class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea, binary search on the rows first to find which row the target is in 
        # then binary search the values of the row

        ### binary search rows
        # initial checks
        if len(matrix) == 0:
            return False

        # classic iterative binary search but on rows
        topRowIdx = len(matrix)-1
        bottomRowIdx = 0
        targetRow = None
        while topRowIdx >= bottomRowIdx:
            if topRowIdx == bottomRowIdx:
                midRow = matrix[topRowIdx]
                if target >= midRow[0] and target <= midRow[-1]:
                    targetRow = matrix[topRowIdx]
                    break
                else:
                    return False

            midRowIdx = bottomRowIdx + (topRowIdx-bottomRowIdx) // 2
            midRow = matrix[midRowIdx]
            # check if possible
            if target >= midRow[0] and target <= midRow[-1]:
                targetRow = midRow
                break
            elif target < midRow[0]:
                topRowIdx = midRowIdx-1
            elif target > midRow[-1]:
                bottomRowIdx = midRowIdx+1
            else:
                return False
        
        ### binary search values
        # initial checks
        if targetRow == None:
            return False
        if len(targetRow) == 0:
            return False
        if len(targetRow) == 1:
            if targetRow[0] == target:
                return True
            else:
                return False

        # classic iterative binary search        
        topIdx = len(targetRow)-1
        bottomIdx = 0
        while topIdx >= bottomIdx:
            # check when equal
            if topIdx == bottomIdx:
                if targetRow[topIdx] == target:
                    return True
                else:
                    return False
            
            # check mid
            midIdx = bottomIdx + (topIdx-bottomIdx) // 2
            mid = targetRow[midIdx]

            if mid == target:
                return True
            elif target > mid:
                # update bottom
                bottomIdx = midIdx+1
            else:
                # update top
                topIdx = midIdx-1
        
        # not possible to be here so return false
        return False