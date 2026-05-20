class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_number = 1
        n = len(nums)
        while min_number in nums:
            min_number += 1
        return min_number
