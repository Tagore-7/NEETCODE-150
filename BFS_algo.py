class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return 
    print(root.val)
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    if not root:
        return 
    inorder(root.left)
    inorder(root.right)
    print(root.val)

