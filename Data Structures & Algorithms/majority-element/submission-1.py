class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] += 1
        maximum = 0
        key = 0
        for i in hashmap:
            if hashmap[i] > maximum:
                maximum = hashmap[i]
                key = i
        return key
