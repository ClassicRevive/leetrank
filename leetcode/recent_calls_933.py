class RecentCounter:
    from collections import deque
    ''' Sliding window problem with memoryless property.
        Since once a ping is old, we will never need it again, we can get rid of it.
        If we needed to retain it, we just use sliding window on an array.    
    '''
    def __init__(self):
        self.counter = 0
        self.requests = deque()
        

    def ping(self, t: int) -> int:
        # every time we get a ping, add it to requests queue
        self.requests.append(t)
        self.counter += 1

        # remove old requests from the queue
        while self.requests[0] < t-3000:
            self.requests.popleft()
            self.counter -= 1
        
        return self.counter





        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)