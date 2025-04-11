# https://neetcode.io/courses/dsa-for-beginners/24
# Time complexity = O(logN)

# For Heaps, always make sure to satisfy below 2 properties:
    # Structure Property -> All nodes should be filled from left to right
    # Order Property -> Follow it as per Min Heap or Max Heap


class Heap:
    def __init__(self):
        # First element of a heap has to be a Zero (in the array representation)
        self.heap = [0]

    def pushMinHeap(self, val):
        # Append the value to end of the heap array
        self.heap.append(val)

        # Put the i pointer to the last element aka the one appended above
        i = len(self.heap) - 1

        # Percolate up by comparing parent node to val using the formula
        # Since this is Min Heap we check if heap[i] < heap[parent] and replace them

        # Max Heap is vice versa 
        # while self.heap[i] > self.heap[i // 2]:

        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2      # Update the i pointer