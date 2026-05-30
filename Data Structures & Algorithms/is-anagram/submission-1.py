class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashCountS, hashCountT = {}, {}

        for i in range(len(s)):
            hashCountS[s[i]] = hashCountS.get(s[i], 0) + 1
            hashCountT[t[i]] = hashCountT.get(t[i], 0) + 1
        
        return hashCountS == hashCountT