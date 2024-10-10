class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# Insert a new node and return the root of the BST 
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if root.val > val:
        root.left = insert(root.left, val)
    elif root.val < val:
        root.right = insert(root.right, val)
    
    return root

# Return the minimum value node of the BST
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

# Remove the node and return the root of the BST
def remove(root, val):
    if not root:
        return None

    if val > root.val:
        root.right =  remove(root.right, val)
    elif val < root.val:
        root.left =  remove(root.left, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            minNode = minValueNode(root.right)
            root.val = minNode.val
            root.right = remove(root.right, root.val)
    return root
