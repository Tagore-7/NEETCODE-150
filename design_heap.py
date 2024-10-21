#Design a Minimum Heap (aka a Priority Queue) class.
#
#Your MinHeap class should support the following operations:
#
#MinHeap() will initialize an empty minimum heap.
#void push(int val) will add val to the heap.
#int pop() will remove and return the smallest element in the heap. If the heap is empty, return -1.
#int top() will return the smallest element in the heap without removing it. If the heap is empty, return -1.
#void heapify(int[] nums) will build a minimum heap from nums.
#Note: push and pop should be implemented in 
#O
#(
#l
#o
#g
#n
#)
#O(logn) time complexity, while top should be implemented in 
#O
#(
#1
#)
#O(1), and heapify should be implemented in 
#O
#(
#n
#)
#O(n) time complexity.
#
#Example 1:
#
#Input:
#["top", "push", 1, "top", "pop", "pop"]
#
#Output:
#[-1, null, 1, 1, -1]
#Example 2:
#
#Input:
#["heapify", [1 2 3 4 5], "pop", "pop", "pop", "pop", "pop"]
#
#Output:
#[null, 1, 2, 3, 4, 5]
#
class MinHeap:

    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i // 2]
            self.heap[i // 2] = self.heap[i]
            self.heap[i] = temp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = temp
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = temp
                i = 2 * i
            else:
                break
        return res

    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        return -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums
        cur = len(self.heap) // 2
        while cur > 0:
            i = cur
            while 2 * i < len(self.heap):
                if 2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = temp
                    i = 2 * i + 1
                elif self.heap[2 * i] < self.heap[i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = temp
                    i = 2 * i
                else:
                    break
            cur -= 1



