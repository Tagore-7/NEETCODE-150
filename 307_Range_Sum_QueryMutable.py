#Given an integer array nums, handle multiple queries of the following types:
#
#Update the value of an element in nums.
#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:
#
#NumArray(int[] nums) Initializes the object with the integer array nums.
#void update(int index, int val) Updates the value of nums[index] to be val.
#int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# 
#
#Example 1:
#
#Input
#["NumArray", "sumRange", "update", "sumRange"]
#[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
#Output
#[null, 9, null, 8]
#
#Explanation
#NumArray numArray = new NumArray([1, 3, 5]);
#numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
#numArray.update(1, 2);   // nums = [1, 2, 5]
#numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
# 
#
#Constraints:
#
#1 <= nums.length <= 3 * 104
#-100 <= nums[i] <= 100
#0 <= index < nums.length
#-100 <= val <= 100
#0 <= left <= right < nums.length
#At most 3 * 104 calls will be made to update and sumRange.
#


class BIT:
    def __init__(self, nums):
        self.n = len(nums) + 1
        self.nums = [0] * self.n
        self.tree = [0] * self.n
        for i in range(self.n - 1):
            self.update(i, nums[i])

    def update(self, index, val):
        index += 1
        diff = val - self.nums[index]
        self.nums[index] = val
        while index < self.n:
            self.tree[index] += diff
            index += index & -index

    def prefix_sum(self, index):
        total_sum = 0
        while index > 0:
            total_sum += self.tree[index]
            index -= index & -index
        return total_sum

    def query(self, left, right):
        return self.prefix_sum(right + 1) - self.prefix_sum(left)


class NumArray:
    def __init__(self, nums: List[int]):
        self.bit = BIT(nums)

    def update(self, index: int, val: int) -> None:
        self.bit.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(left, right)
