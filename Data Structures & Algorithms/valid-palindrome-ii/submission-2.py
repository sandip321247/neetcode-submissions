class Solution:
    def validPalindrome(self, s: str) -> bool:
        mistake = 0
        # s = "".join(ch.lower() for ch in s if ch.isalnum())
        l , r = 0 ,len(s)-1
        while l < r:
            if s[l] != s[r]:
                skipleft , skipright = s[l+1 : r+1] , s[l : r]
                return (skipleft == skipleft[::-1]) or (skipright == skipright[::-1])
                    
                
            l += 1
            r -= 1
        return True