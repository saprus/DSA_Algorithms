
"""
https://neetcode.io/courses/dsa-for-beginners/23
Check notes in the link (scroll below the video)

# For Heaps, always make sure to satisfy below 2 properties:
    # Structure Property -> All nodes should be filled from left to right
    # Order Property -> Follow it as per Min Heap or Max Heap

Time Complexity:
Get Min/Max     -> O(1)
Push/Pop        -> O(logN)
Heapify         -> O(n)
    

In heap priority queue sole purpose is to get Min/Max value

- Two Types of Heaps: Min Heap and Max Heap
    Min heaps have the smallest value at the root node. 
    The smallest value has the highest priority to be removed.

    Max heaps have the largest value at the root node. 
    The largest value has the highest priority to be removed.
    


Max Heap: Every node is greater than both its childs
Min Heap: Vice versa

If you were to put the nodes in an array from left to right 
on each level and leave index 0 empty
The you can access the leftChild, rightChild, parent nodes using this formula

leftChild = 2 * i
rightChild = 2 * i + 1
parent = i / 2

Check Indexing-Of-Heap.png and apply this formaula for indexes
"""