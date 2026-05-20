class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l = 0
        r = x
        while l <= r:
            mid = (r+ l)//2
            if mid ** 2 == x:
                ans = mid
                return ans
            elif mid ** 2 > x:
                r = mid -1
            else:
                l = mid + 1
                ans = mid
        return ans
