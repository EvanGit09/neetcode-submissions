class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counthash = {}
        for i in nums:
            counthash[i] = counthash.get(i, 0) + 1
        print("counthash: ", counthash)

        counthashSorted = {k: v for k, v in sorted(counthash.items(), reverse=True, key=lambda item: item[1])}
        print("counthashSorted: ", counthashSorted)

        outputList = list(counthashSorted.keys())[0:k]
        print("outputList: ", outputList)
        return outputList
