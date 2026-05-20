class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res , sol = [],[]
        hashmap = {n:0 for n  in nums}
        for i in nums:
            hashmap[i] += 1
        

        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return 

            for  i in hashmap :
                if hashmap[i] > 0:
                    hashmap[i] -= 1
                    sol.append(i)

                    backtrack()

                    hashmap[i]+= 1
                    sol.pop()
        backtrack()

        return res

            

            
