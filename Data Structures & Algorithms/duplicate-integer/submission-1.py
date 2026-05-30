class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            strNum = str(i)
            try:
                if hashmap[strNum]:
                    return True
            except:
                hashmap[strNum] = strNum

        return False