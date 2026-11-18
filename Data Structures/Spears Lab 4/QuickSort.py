#Imports numpy for the median of three calculations, and my Counter class
import numpy as np
from Counter import *

#Initializes a Counter to be used for quicksort functions
quickCounter = Counter()

#The 'default' partition function that selects the first item as the pivot
def PartitionDefault(array, low, high):
    pivot = array[low]
    while(True):
        while(array[low] < pivot):
            low += 1
            quickCounter.incrementComparisons()
        while(array[high] > pivot):
            high -= 1
            quickCounter.incrementComparisons()
        if (low >= high):
            return high
        else:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp
            quickCounter.incrementExchanges()

#The median of three partitions function that selects the median of first, last, and middle index as the pivot
def PartitionMedianOfThree(array, low, high):
    middleIndex = (low + high) // 2
    pivotChoices = [array[low], array[middleIndex], array[high]]
    pivot = np.median(pivotChoices)

    while (True):
        while (array[low] < pivot):
            low += 1
            quickCounter.incrementComparisons()
        while (array[high] > pivot):
            high -= 1
            quickCounter.incrementComparisons()
        if (low >= high):
            return high
        else:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp
            quickCounter.incrementExchanges()

#The 'default' quicksort function that uses partitions of size 1 and 2 as the base cases.
def QuickSortDefault(array, low, high):
    if((low-high >= -1)):
        return

    partitionIndex = PartitionDefault(array, low, high)
    QuickSortDefault(array, low, partitionIndex)
    QuickSortDefault(array, partitionIndex + 1, high)

#The quicksort function that implements median of three partitioning
def QuickSortMedianOfThree(array, low, high):
    if((low-high >= -1)):
        return

    partitionIndex = PartitionMedianOfThree(array, low, high)
    QuickSortMedianOfThree(array, low, partitionIndex)
    QuickSortMedianOfThree(array, partitionIndex + 1, high)

#The quicksort function that stops at the user inputted limit to finish with insertion sort
def QuickSortWithInsertion(array, low, high, limit):
    if(low-high >= -(limit-1)):
        InsertionSort(array, low, high)
        return

    partitionIndex = PartitionDefault(array, low, high)
    QuickSortWithInsertion(array, low, partitionIndex, limit)
    QuickSortWithInsertion(array, partitionIndex + 1, high, limit)


#The insertion sort function
def InsertionSort(array, lowIndex, highIndex):
    lenSortedPortion = lowIndex
    for i in range(lowIndex, highIndex+1):
        key = array[i]
        spot = 0
        for j in range(lenSortedPortion):
            if key > array[j]:
                spot += 1
                quickCounter.incrementComparisons()
            else:
                quickCounter.incrementComparisons()
                break
        array.pop(i)
        array.insert(spot, key)
        lenSortedPortion += 1
        quickCounter.incrementExchanges()
    return
