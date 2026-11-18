from Populate import *
from QuickSort import *
from MergeSort import *
import sys

#Increases the recursion limit set by Pycharm. The natural merge function reaches maximum recursion depth for files greater than 2000 items if this is not implemented.
sys.setrecursionlimit(10000)

#A function used for making output files when a quicksort was used
def printQuickSort(array):
    with open("output.txt", "w") as File:
        for element in array:
            File.write(str(element))
            File.write("\n")
        File.write("Comparisons: " + str(quickCounter.comparisons) + "\n")
        File.write("Exchanges: " + str(quickCounter.exchanges) + "\n")

#A function used for making output files when natural merge was used
def printMergeSort(array):
    with open("output.txt", "w") as File:
        for element in array:
            File.write(str(element))
            File.write("\n")
        File.write("Comparisons: " + str(mergeCounter.comparisons) + "\n")
        File.write("Exchanges: " + str(mergeCounter.exchanges) + "\n")

#The main function
def main():
    #Array of possible file size selections
    fileSizes = [50, 1000, 2000, 5000, 10000]

    #Populates all file sizes and types
    repopulate()

    #Gets the file size as an input from the user
    fileSize = 0
    while(fileSize not in fileSizes):
        fileSize = int(input("Enter file size to be sorted from these options: 50, 1000, 2000, 5000, 10000 \n"))


    #Get file extension from user and read data into an array so long as that extension was entered correctly
    inputFile = input("Enter file extension (inOrder.txt, reverseOrder.txt, or random.txt)\n")
    inputFile = str(fileSize) + "_" + inputFile
    try:
        with open(inputFile, "r") as File:
             numbers = File.readlines()
    except:
        print("Error: inappropriate extension")
        return 1 #Error code 1 indicates file extension was typed in incorrectly

    #Strips the elements in numbers and converts them to integers
    for i in range(len(numbers)):
        numbers[i] = numbers[i].rstrip("\n")
        numbers[i] = int(numbers[i])

    SortType = int(input("Select the number for the type of sorting you wish to perform:\n1)Default Quicksort\n2)Quicksort Median of Three\n3)Quicksort that sorts partitions of size 50 or less with Insertion Sort\n4)Quicksort that sorts partitions of size 100 or less with Insertion Sort\n5)Natural Merge Sort\n"))
    if(SortType == 1):
        QuickSortDefault(numbers, 0, len(numbers) -1)
        printQuickSort(numbers)
    elif(SortType == 2):
        QuickSortMedianOfThree(numbers, 0, len(numbers) -1)
        printQuickSort(numbers)
    elif(SortType == 3):
        QuickSortWithInsertion(numbers, 0, len(numbers) -1, 50)
        printQuickSort(numbers)
    elif(SortType == 4):
        QuickSortWithInsertion(numbers, 0, len(numbers) - 1, 100)
        printQuickSort(numbers)
    elif(SortType == 5):
        partitions = getPartitions(numbers)
        NaturalMerge(numbers, partitions)
        printMergeSort(numbers)
    else:
        print("Error: Incorrect Selection")
        return 2 #Error code 2 indicates sort type was typed in incorrectly

    return 0

#Call to the main function
main()
