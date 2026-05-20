class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listToSet = set(nums)
        if len(nums) == len(listToSet):
            return False
        else:
            return True
         