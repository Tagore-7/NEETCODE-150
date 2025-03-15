#Binary Tree Node
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val 
        self.left = left 
        self.right = right


def inorder(root):
    stack = []
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right

def preorder(root):
    stack = []
    curr = root

    while stack or root:
        if curr:
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            curr = curr.left 
        else:
            curr = stack.pop()

def postorder(root):
    stack = [root]
    visit = [False]

    while stack:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                stack.append(curr)
                visit.append(True)
                stack.append(curr.right)
                visit.append(False)
                stack.append(curr.left)
                visit.append(False)
