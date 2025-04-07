"""
Depth First Search
- Traversal can be done in 3 ways: Preorder, Inorder, Postorder
"""


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
