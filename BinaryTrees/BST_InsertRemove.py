"""
Binary Search Tree - Insert and Remove

IMPORTANT Algorithm - watch video to refresh memory
    https://neetcode.io/courses/dsa-for-beginners/18

Why not have the a Sorted array vs Binary search tree?
    Traversing to find an element is still O(n) in both
    But the real difference is in Insertion and Removal
    BST have O(logn) and array have O(nlogn)
"""

def insert(root, val):    
    if root is None:
        return TreeNode(val)
    
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root

def remove(root, val):

    if root is None:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    # Up till here, we are just trying to locate the node which is equal to "val"

    else:
        # Found the val to be removed
        if not root.right:
            return root.left        # For 1 child node only
        elif not root.left:
            return root.right       # For 1 child node only
        else:
            # For 2 child nodes

            ## IMPORTANT ##
            # We only need minNode's Value to replace it with the root.val
            minNode = minValueNodeIterative(root.right)
            root.val = minNode.val

            # Make sure to have it assigned to root.right
            # Or else you will lose the updated tree structure
            # FOR DEMO: Draw a 5 depth tree, and make sure the minNode 
            # has a right node ATLEAST to go through this scenario
            root.right = remove(root.right, minNode.val)

    return root
        

def minValueNodeIterative(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    
    return curr
    
    # The below way is correct too
    # But it doesn't preserve "root" in case you want to return root
    # Use the above way, curr = root
    while root.left:
        root = root.left
    return root

def minValueNodeRecursive(root):
    """
    In recursive, we don't need to do curr = root
    Because in recursion, you're preserving "root"
    as you're just going down the stack call 
    """
    if root.left is None:
        return root
    
    return minValueNodeRecursive(root.left)