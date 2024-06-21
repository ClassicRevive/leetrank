# Using unique constraint with a python-native heap using hashset.
# Supplementing current_integer count with a heap.

import heapq as hq

class SmallestInfiniteSet:
    def __init__(self):
        self.current_int = 1
        self.heap: [int] = []
        self.is_present: {int} = set()

    def popSmallest(self) -> int:
        if len(self.heap):  # if there are elements in the heap, pop these first
            num = hq.heappop(self.heap)
            self.is_present.remove(num)
        else:  # otherwise, use current integer
            num = self.current_int
            self.current_int += 1

        return num

    def addBack(self, num: int) -> None:
        if num < self.current_int and num not in self.is_present:
            hq.heappush(self.heap, num)
            self.is_present.add(num)


if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    
    to_pop = 5
    for i in range(to_pop):
        num = obj.popSmallest()
        print(f"Popped {num}")

    obj.addBack(2)
    obj.addBack(1)
    print("Added back 2 and 1")

    num = obj.popSmallest()
    print(f"Smallest: {num}")