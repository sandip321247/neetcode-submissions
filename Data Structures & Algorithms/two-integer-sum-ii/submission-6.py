class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l <= len(numbers):
            for r in range(l+1 ,len(numbers)):
                
                if numbers[l] + numbers[r] == target :
                    return [l+1 , r+1]
            l+=1
        return []