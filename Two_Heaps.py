import heapq

class Median:
    def __ini__(self):
        self.small = []
        self.large = []


    def insert(self, num):
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            val  = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heapop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def getMedian(self):
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
