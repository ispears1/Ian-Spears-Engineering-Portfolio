from HuffmanFunctions import *
#imports functions from HuffmanFunctions.py

with open('FreqTable.txt', "r") as Table:
    Frequencies = Table.readlines()
    # Read the lines of the FreqTable.txt file as a list named 'Frequencies'

FrequencyDict = {}
# Define a dictionary named FrequencyDict

for line in Frequencies:
    letter, frequency = line.split("-")
    letter = letter.strip()
    frequency = frequency.strip()
    frequency = int(frequency)
    FrequencyDict[letter] = frequency
    # Take the letter and frequency combinations from Frequencies and store them in the FrequencyDict Dictionary

HuffmanTree = BuildCodedTree(FrequencyDict)
#Creates a huffman tree from the frequency dictionary and calling BuildCodedTree()
HuffmanCodes = {}
HuffmanCodes = GetTreeCodes(HuffmanTree, "", HuffmanCodes)
#Creates a dictionary of huffman codes using the huffman tree and calling GetTreeCodes()

EncodingFile = input("Enter the name of the file containing phrases you wish to encode (including the extension): ")
#Takes an input from the user for the text file name of phrases they wish to encode
with open(EncodingFile, "r") as thisFile:
    phrases = thisFile.readlines()
    #reads lines into a list 'phrases'
with open("EncodingOutput.txt", "w") as thatFile:
    for line in phrases:
        thatFile.write(Encode(HuffmanCodes, line))
        thatFile.write("\n")
        #calls the Encode() function to encode the elements in phrases, also writes a new line after

DecodingFile = input("Enter the name of the file containing phrases you wish to decode (including the extension): ")
#Takes an input from the user for the text file name of phrases they wish to decode
with open(DecodingFile, "r") as anotherFile:
    codes = anotherFile.readlines()
    #reads lines into a list 'codes'
with open("DecodingOutput.txt", "w") as finalFile:
    for line in codes:
        finalFile.write(Decode(HuffmanTree, line))
        finalFile.write("\n")
        #calls the Decode() function to decode the elements in codes, also writes a new line after