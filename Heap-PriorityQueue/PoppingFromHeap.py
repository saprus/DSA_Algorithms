# https://neetcode.io/courses/dsa-for-beginners/24
# Time Complexity = O(logN)

# For Heaps, always make sure to satisfy below 2 properties:
    # Structure Property -> All nodes should be filled from left to right
    # Order Property -> Follow it as per Min Heap or Max Heap

# Popping from Min Heap
    # Pop the top element
    # Replace it with the last element
    # Now constantly compare it with its children and keep replacing with the least value child 
    # This is so that it satisfies the Min Heap property

def pop(self):
    if len(self.heap) == 1:
        # No element other than just the [0] aka empty Heap
        return None
    if len(self.heap) == 2:
        # Only 1 element [0, element] -> so we just simply pop the last element
        return self.heap.pop()

    res = self.heap[1]   
    # Move last value to root
    self.heap[1] = self.heap.pop()
    i = 1

    # Percolate down
    # self.heap[2 * i] means left child
    # self.heap[2 * i + 1] means right child 

    # Heaps are filled left to right, so we run the loop till no left child 
    while 2 * i < len(self.heap):

        if (2 * i + 1 < len(self.heap) and 
        self.heap[2 * i + 1] < self.heap[2 * i] and 
        self.heap[i] > self.heap[2 * i + 1]):
            # Swap right child
            tmp = self.heap[i]
            self.heap[i] = self.heap[2 * i + 1]
            self.heap[2 * i + 1] = tmp
            i = 2 * i + 1

        elif self.heap[i] > self.heap[2 * i]:
            # Swap left child
            tmp = self.heap[i]
            self.heap[i] = self.heap[2 * i]
            self.heap[2 * i] = tmp
            i = 2 * i
        
        else:
            break
    return res