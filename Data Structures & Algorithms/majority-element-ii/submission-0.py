class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap  = {}
        res = []
        n = len(nums)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] > n/3:
                res.append(i)
        return res