class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        part = []

        def isPallindrom(s,l , r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l , r = l+1 , r-1
            return True

        def backtrack(i):
            if i == n:
                res.append(part.copy())
                return 

            for j in range(i , n):
                if isPallindrom(s,i,j ):
                    part.append(s[i:j+1])
                    backtrack(j+1)
                    part.pop()

        backtrack(0)
        return res