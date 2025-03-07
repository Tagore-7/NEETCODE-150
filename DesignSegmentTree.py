#Design a Segment Tree class.
#
#Your SegmentTree class should support the following operations:
#
#SegmentTree(int[] arr) will initialize a segment tree based on the given array arr. You can assume that the array arr is non-empty.
#int query(int l, int r) will return the sum of all elements in the range [l, r] inclusive. You can assume that 0 <= l <= r < arr.length.
#void update(int idx, int val) will update the element at index idx in the original array to be val. You can assume that 0 <= idx < arr.length.
#Example 1:
#
#Input:
#["SegmentTree", [1, 2, 3, 4, 5], "query", 0, 2, "query", 2, 4, "update", 3, 0, "query", 2, 4]
#
#Output:
#[null, 6, 12, null, 8]
#Example 2:
#
#Input:
#["SegmentTree", [-1, 2, 4], "query", 0, 1, "query", 1, 2, "update", 2, 3, "query", 0, 2]
#
#Output:
#[null, 1, 6, null, 4]
#
class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)

        M = (L + R) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root, index, val):
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        if index > M:
            self.update_helper(root.right, index, val)
        else:
            self.update_helper(root.left, index, val)
        root.sum = root.left.sum + root.right.sum


    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root, L, R):
        if L <= root.L and root.R <= R:
            return root.sum

        if R < roo.L or L > root.R:
            return 0

        return self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R)



