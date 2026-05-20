class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(ch.lower() for ch in s if ch.isalnum())
        l , r = 0 , len(s)-1
        is_palindrome = True
        while l <= r:
            if s[l] != s[r]:
                is_palindrome = False
            l += 1
            r -=1
        return is_palindrome
