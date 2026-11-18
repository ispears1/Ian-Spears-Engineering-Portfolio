from Counter import *

#Initializes the counter to be used for natural merge
mergeCounter = Counter()

#The node class to be implemented in the linked lists
class Node():

    def __init__(self, num):
        self.num = num
        self.next = None

#The linked list class to be used in merging
class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def getHead(self):
        if (self.head == None):
            print("Error Empty List")
            return
        else:
            return self.head

    def append(self, num):
        new_node = Node(num)
        if(self.head is None):
            self.head = new_node
            self.tail = new_node
        if(self.head.next is None):
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if(self.head is None):
            print("Error Empty List")
            return
        else:
            temp = self.head
            self.head = self.head.next
            return temp.num


#The merge function that replaces sections of an array with the merged, in order version of itself
def Merge(array, section1Start, section2Start, section2End):
    merged = LinkedList()
    mergedSize = 0
    section1Index = section1Start
    section2Index = section2Start
    while(section1Index < section2Start and section2Index < section2End):
        if(array[section1Index] < array[section2Index]):
            merged.append(array[section1Index])
            section1Index += 1
            mergedSize += 1
            mergeCounter.incrementComparisons()
        else:
            merged.append(array[section2Index])
            section2Index += 1
            mergedSize += 1
            mergeCounter.incrementComparisons()
    while(section1Index < section2Start):
        merged.append(array[section1Index])
        section1Index += 1
        mergedSize += 1
    while(section2Index < section2End):
        merged.append(array[section2Index])
        section2Index += 1
        mergedSize += 1

    for i in range(mergedSize):
        array[section1Start + i] = merged.pop()
        mergeCounter.incrementExchanges()

    return

#The natural  merge function that recursively merges larger and larger partitions
def NaturalMerge(array, partitions_array):
    length = len(partitions_array)
    if(length <= 2):
        return
    if(length == 3):
        Merge(array, partitions_array[0], partitions_array[1], partitions_array[2])
        return
    else:
        Merge(array, partitions_array[0], partitions_array[1], partitions_array[2])
        partitions_array.pop(1)
        length -= 1
        Merge(array, partitions_array[length-3], partitions_array[length-2], partitions_array[length-1])
        partitions_array.pop(length-2)
        return NaturalMerge(array, partitions_array)

#The function that finds sections of the array that are already in order for the natural merge function
def getPartitions(array):
    partitions = [0]
    for i in range(len(array)-1):
        mergeCounter.incrementComparisons()
        if(array[i] > array[i+1]):
            partitions.append(i+1)
    partitions.append(len(array))
    return partitions
