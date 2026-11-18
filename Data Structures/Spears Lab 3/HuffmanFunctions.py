from TreeFunctions import *
#imports the functions from TreeFunctions.py

def stringToHex(string):
    #A function that converts a string to an integer based on the ordinal values of its characters
    #Used for decided which elements should be placed at left or right nodes.
    total = 0
    for letters in string:
        total += ord(letters)
    return total

#This function builds a Huffman Tree from a dictionary of letters and associated frequencies
def BuildCodedTree(Dictionary):
    # This section of code creates TreeArray, and then creates Trees with each letter and its associated frequency
    TreeArray = []
    for key in Dictionary:
        TreeArray.append(Tree(key, Dictionary[key]))


    while(len(TreeArray) > 1):
        min = 1000
        min2 = 1000
        #min1 and min2 are arbitrarily large numbers, and would need to be increased depending the frequencies in FreqTable
        leftChild = ""
        rightChild = ""
        # This section finds the lowest frequency letter/phrase, and removes it from TreeArray. This is defined as the left Child
        for element in TreeArray:

            if(element.frequency < min):
                min = element.frequency
                leftChild = element
        TreeArray.remove(leftChild)

        # This section finds the next lowest frequency letter/phrase, and removes it from TreeArray. This is defined as the right Child
        for next_element in TreeArray:
            if (next_element.frequency < min2):
                min2 = next_element.frequency
                rightChild = next_element
        TreeArray.remove(rightChild)

        #If the two frequencies are the same, then the algorithm defers to the tiebreaker of the left child having a lower ordinal value
        #This is done with the stringToHex() function defined above
        if(min == min2):
            if(stringToHex(leftChild.letter) > stringToHex(rightChild.letter)):
                temp = leftChild
                leftChild = rightChild
                rightChild = temp

        #The final section of code creates a new Tree from the sorted letters and combined frequencies of leftChild and rightChild.
        #It then takes this new tree, appends left and right child in the correct locations, and pushes the whole tree back in
        #to the tree array.
        newVar = leftChild.letter + rightChild.letter
        newVar = ''.join(sorted(newVar))
        totalFreq = leftChild.frequency + rightChild.frequency
        temp = Tree(newVar, totalFreq)
        temp.left = leftChild
        temp.right = rightChild
        TreeArray.append(temp)

    #returns the Huffman Tree
    return TreeArray[0]

#A function that recursively determines Huffman Codes from the Huffman Tree and stores them in a dictionary with the letter as the key
def GetTreeCodes(TreeNode, code, CodeDict):
    if(TreeNode.left == None and TreeNode.right == None):
        CodeDict[TreeNode.letter] = code
    else:
        GetTreeCodes(TreeNode.left, code + "0", CodeDict)
        GetTreeCodes(TreeNode.right, code + "1", CodeDict)

    return CodeDict

#A function that Decodes Huffman Codes by following the Huffman Tree to its leaves.
def Decode(Root, string):
    node = Root
    output = ""
    string = string.strip()
    #Checks for letters and any characters that are not 0 or 1
    if any(char.isalpha() for char in string):
        return "Error: Huffman Codes should not contain letters"
    if any(char != '0' and char != '1' for char in string):
        return "Error: Unrecognized character"

    for letter in string:
        if letter == '0':
            node = node.left
        if letter == '1':
            node = node.right

        if(node.left == None and node.right == None):
            output += node.letter
            node = Root

    return output

#A code that encodes phrases based on the Dictionary obtained from GetTreeCodes()
def Encode(Dictionary, string):
    string = string.upper()
    string = string.replace(" ", "")
    output = ""
    #Checks for digits
    if(any(char.isdigit() for char in string)):
        return "Error: Please ensure the input is not a Huffman Code. Otherwise, this program does not contain codes for numbers."

    while(len(string) > 0):
        if(string[0].isalpha()):
            output += Dictionary[string[0]]
            string = string[1:]
        else:
            string = string[1:]
    return output