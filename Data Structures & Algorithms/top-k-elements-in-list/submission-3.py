class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i , 0) + 1
        sorted_dict = dict(sorted(hashmap.items() , key = lambda x:x[1] , reverse = True))
        return list(sorted_dict.keys())[:k]
        
            
