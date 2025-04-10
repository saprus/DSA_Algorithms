# https://neetcode.io/courses/dsa-for-beginners/20
# Time complexity -> O(n)
from collections import deque

def bfs(root):

    # This is a Double Ended Queue
    # First in First out
    queue = deque()

    if root:
        # Appends just the root node, which has the 
        # pointers to its left and right childs.. and then they have the same
        # So the len(queue) at this point is 1 as it just has the root node
        queue.append(root)
    
    while queue:
        curr = queue.popleft()
        print(curr.val)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    