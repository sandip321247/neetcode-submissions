class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res , sol = [],[]

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            #aage badhe hum but koi value add nahi kiye
            backtrack(i+1)

            #aage badhe but hum value add kiye
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res
            

