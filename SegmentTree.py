class SegementTree:
    def __init__(self, total, L, R):
        self.total = total 
        self.left = None 
        self.right = None 
        self.L = L
        self.R = R 

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegementTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegementTree(0, L, R) 
        root.left = SegementTree.build(nums, L, M) 
        root.right = SegementTree.build(nums, M + 1, R) 
        root.sum = root.left.sum + root.right.sum
        return root 

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val 
            return 

        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val) 

        self.sum = self.left.sum + self.right.sum


    def rangeQuery(self, L, R):
        if L == self.L and R == self.R:
            return self.sum 

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R) 
        else:
            return (self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R))

