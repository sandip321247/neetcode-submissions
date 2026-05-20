class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l , r = 0 ,0
        res = ""
        while l <= len(word1) -1 and r <= len(word2) -1:
            res += word1[l]
            res += word2[r]
            l += 1
            r += 1

        if l <= len(word1)-1:
            res += word1[l:len(word1)]

        if r <= len(word2)-1:
            res += word2[l:len(word2)]

        return res