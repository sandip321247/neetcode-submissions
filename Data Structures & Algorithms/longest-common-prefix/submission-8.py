class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        length = len(strs[0])
        i = 0
        for i in range(length):
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]   :
                    return "".join(res)
            res.append(strs[0][i])
            i += 1
        
        return "".join(res)
