class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res , sol = [],[]

        if n == 0:
            return [[]]

        def backtrack():
            if len(sol) == n:
                res.append(sol.copy())
                return

            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()

        backtrack()
        return res
        