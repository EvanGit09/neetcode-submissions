class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, item in enumerate(nums):
            curr = hashmap.get(item, [])
            curr.append(i)
            hashmap[item] = curr

        print(hashmap)

        for i in range(len(nums)):
            num = nums[i]
            numNeeded = target - num
            indexesArr = hashmap.get(numNeeded, [])
            print(indexesArr)
            if i in indexesArr:
                indexesArr.remove(i)
            print(indexesArr)
            if len(indexesArr) > 0:
                idx = indexesArr[0]
                if i < idx:
                    return [i, idx]
                else:
                    return [idx, i]