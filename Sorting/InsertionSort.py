def insertionSort(nums):
    for i in range(1, len(nums)):
        j = i 
        while j > 0 and nums[j-1] > nums[j]:
            tmp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = tmp

            j -= 1
    return nums

print(insertionSort([4,3,2,1]))