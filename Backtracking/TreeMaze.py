# Backtracking 

"""
If the problem requires a clear "yes or no" answer, 
such as "Does a path exist?" or "Is this condition met?", 
you should return a boolean.

else return None
"""


# Determine if a path exists from the root of the 
# tree to a leaf node. It may not contain any zeroes.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def treeMaze(root):
    # Base case
    if not root or root.val == 0:
        return False
    
    if not root.left and not root.right:
        return True
    
    # Recursive case
    left = treeMaze(root.left)
    right = treeMaze(root.right)

    # Combine case
    # Whichever returns True, means path exists
    return left or right



root = TreeNode(4)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.right = TreeNode(7)
root.right.left = TreeNode(2)
root.right.right = TreeNode(0)

print("Result: " , treeMaze(root))
