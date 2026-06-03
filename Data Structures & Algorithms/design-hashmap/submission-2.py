class ListNode:
    def __init__(self , key = -1 , value = -1):
        self.key = key
        self.value =value
        self.Next = None

class MyHashMap:

    def __init__(self):
        self.HashMap = [ListNode(0,0) for _ in range(10000)]
        
    def hash(self ,  key):
        return key % (len(self.HashMap))
    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        curr = self.HashMap[idx]
        if not curr.Next:
            curr.Next = ListNode(key , value) 
        else:
            curr.Next = None
            curr.Next = ListNode(key , value)

    def get(self, key: int) -> int:
        idx = self.hash(key)
        curr = self.HashMap[idx]
        if curr.Next:
            return curr.Next.value
        else:
            return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.HashMap[idx]
        if curr.Next:
            curr.Next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)