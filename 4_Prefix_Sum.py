# code for calculating prefix sum and  sub range sum in arrays 

class Prefix:
    def __init__(self, array):
        self.prefix = []
        total = 0
        for i in range(array):
            total += array[i]
            self.prefix[i] = total 

    def subarraySum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 1 else 0
        return preRight - preLeft 


