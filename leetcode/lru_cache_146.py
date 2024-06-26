''' Using DLL to represent an LRU cache. Use hashmap to store references to the nodes'''
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key

class LRUCache:
    def add(self, node):
        # adds a node to the tail of linked list O(1)
        real_tail = self.tail.prev
        
        real_tail.next = node
        node.prev = real_tail
        
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        # remove node from linked list O(1) for DLL
        node.prev.next = node.next
        node.next.prev = node.prev
    

    def __init__(self, capacity: int):
        self.head = Node(999, 999)
        self.tail =  Node(999, 999)
        self.capacity = capacity
        self.dict = dict()
        self.size = 0

        # set up the sentinels on initialisation
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        # otherwise, find node in dictionary and add it to the back of DLL
        node = self.dict[key]
        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:  # if not in cache, create new node and add it
            node = Node(key, value)
            self.add(node)
            self.dict[key] = node
            self.size += 1
        else:  # if already in cache, update value in cache and bring to back of LL
            node = self.dict[key]
            node.val = value
            self.remove(node)
            self.add(node)
        
        if self.size > self.capacity:
            to_delete = self.head.next
            self.remove(to_delete)
            del self.dict[to_delete.key]
            self.size -= 1

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)