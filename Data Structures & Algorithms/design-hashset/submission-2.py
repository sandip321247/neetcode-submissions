class ListNode:
    def __init__(self , key = -1  , Next = None):
        self.key = key
        self.Next = Next

class MyHashSet:

    def __init__(self):
        self.HashSet = [ListNode(0) for _ in range(10000)]   
        #ListNode(0) is a dummy node
        
    def add(self, key: int) -> None:
        idx = key % (len(self.HashSet))
        curr = self.HashSet[idx]  #pointing to the dummy node at given index
        
        while curr.Next:
            if curr.Next.key == key:
                return
            curr = curr.Next
        # now curr will be pointing at the last node of that index
        curr.Next = ListNode(key)

    def remove(self, key: int) -> None: 
        idx = key % (len(self.HashSet))
        curr = self.HashSet[idx]

        while curr.Next:
            if curr.Next.key == key:
                curr.Next = curr.Next.Next # bypass the target node
                return
            curr = curr.Next
        
    def contains(self, key: int) -> bool:
        idx = key % (len(self.HashSet))
        curr = self.HashSet[idx]

        while curr.Next:
            if curr.Next.key == key:
                return True
            curr = curr.Next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)