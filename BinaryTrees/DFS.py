"""
Depth First Search
- Traversal can be done in 3 ways: Preorder, Inorder, Postorder
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    if root is None:
        return
    
    # We go Current, Left, Right -> [C]LR
    print(root.val)     # To print them in the CLR order
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    
    # We go left, current, right -> L[C]R
    inorder(root.left)
    print(root.val)     # To print them in the LCR order
    inorder(root.right)


def postorder(root):
    if root is None:
        return 
    
    # We go Left, Right, Current -> LR[C]
    postorder(root.left)
    postorder(root.right)
    print(root.val)     # To print them in the LRC order


# Example tree construction
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(7)
root.left.right = TreeNode(8)
root.right.left = TreeNode(1)

print(inorder(root))