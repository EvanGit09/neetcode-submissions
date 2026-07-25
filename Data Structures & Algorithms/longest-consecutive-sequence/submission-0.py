class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set
        numsSet = set(nums)
        longest = 0

        for num in nums:
            # check if num - 1 is in the set
            # if yes then we need to keep going to find the start value
            # if no then its the start of a sequence
            if not (num-1) in numsSet:
                curr = 0
                currNum = num
                while (currNum) in numsSet:
                    curr += 1
                    currNum += 1
                # we've now find the longest sequence with this starting num
                if curr > longest:
                    longest = curr
                # now repeat for all starting nums we find
            
        
        return longest