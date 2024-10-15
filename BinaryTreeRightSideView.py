#You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.
#
#Example 1:
#
#
#
#Input: root = [1,2,3]
#
#Output: [1,3]
#Example 2:
#
#Input: root = [1,2,3,4,5,6,7]
#
#Output: [1,3,7]
#Constraints:
#
#0 <= number of nodes in the tree <= 100
#-100 <= Node.val <= 100
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)

        rightSideValues = []

        while len(deque):
            rightNode = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    rightNode = curr
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            rightSideValue.append(rightNode.val)

        return rightSideValues 

