class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted = sorted(list(s))
        tSorted = sorted(list(t))
        if sSorted == tSorted:
            return True
        else:
            return False