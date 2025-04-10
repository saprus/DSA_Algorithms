# Backtracking

# Determine if a path exists from the root of the 
# tree to a leaf node. It may not contain any zeroes.
# If yes, return the path with values

# Time complexity -> O(n)

def leafPath(root, path):

    # Base Case
    if root is None or root.val == 0:
        return False
    
    path.append(root.val)

    if not root.left and not root.right:
        return True

    # Recursive Case
    left = leafPath(root.left, path)
    right = leafPath(root.right, path)

    # Combine Case
    if left or right:
        return True
    
    path.pop()
    return False   # Make a note of this - we need to explicitly return False when using "path"