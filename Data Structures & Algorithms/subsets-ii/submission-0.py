class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res , sol = [],[]

        def backtrack(i):
            if i == n:
                
                res.append(sol.copy())
                return 

            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        s = set(tuple(sorted(row)) for row in res)
        lst = [list(i) for i in s]

        return lst

