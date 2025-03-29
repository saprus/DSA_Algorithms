# Binary Search Tree - Insert and Remove

# IMPORTANT Algorithm - watch video to refresh memory
    # https://neetcode.io/courses/dsa-for-beginners/18

# Why not have the a Sorted array vs Binary search tree?
    # Traversing to find an element is still O(n) in both
    # But the real difference is in Insertion and Removal
    # BST have O(logn) and array have O(nlogn)

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
    # Thats why we recursively call the remove() to find that node
    # Now, below we are going to try to remove that particular node
    else:
        # We are in here because the node value == val
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNodeIterative(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)

    return root



def minValueNodeIterative(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    
    return curr
    
    # This way is correct too
    # But this doesn't preserve "root" in case you want to return root
    # Use the above way, curr = root
    while root.left:
        root = root.left
    return root

def minValueNodeRecursive(root):
    # In recursive, we don't need to do curr = root
    # Because in recursion, you're preserving "root"
    # as you're just going down the stack call
    if root.left is None:
        return root
    
    return minValueNodeRecursive(root.left)

def minValue(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    
    return curr