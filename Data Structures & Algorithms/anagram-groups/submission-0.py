class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = []
        for strX in strs:
            sortedStrs.append("".join(sorted(strX)))
        print("sortedStrs: ", sortedStrs)

        outputDict = {}
        for i, sortedX in enumerate(sortedStrs):
            a = outputDict.get(sortedX, False)
            if a == False:
                a = [strs[i]]
            else:
                a.append(strs[i])
            outputDict[sortedX] = a
        print("outputDict: ", outputDict)
        print("outputDict.values(): ", outputDict.values())
        return list(outputDict.values())