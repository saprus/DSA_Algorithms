# Binary Search Tree is just a SORTED version of a Binary Tree

# O(n) - worst case
# O(logn) - average case
def search(root, target):
    if root is None:
        # termination case
        return None
    
    if root.val < target:
        return search(root.right, target)
    elif root.val > target:
        return search(root.left, target)
    else:
        return True
