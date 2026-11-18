#This program takes in text files containing prefix alphabetical
#expressions, and returns a new text file containing those expressions
#in postfix format. It does this through the implementation of a stack
#which is in turn populated by nodes. The stack class contains push, pop
#print, and initialization functions. The node class only contains
#an initialization function. The PreToPost conversion function
#pushes letters to the stack, pops two letters and appends the operator
#when an operator is encountered, and handles all other miscellaneous input.
#The main function reads in a text file based on a name from user input,
#and outputs a text file called 'Output.txt'.



#Node class, implemented in the Stack class and its methods
class Node:
    #Constructor method
    def __init__(self):
       self.char = ""
       self.next = None
       # Creates an empty node with no 'next' pointer

#Stack Class
class Stack:

    #Constructor method, creates an empty stack
    def __init__(self):
        self.head_node = None
        # Creates an empty head node

    #Method that checks if the stack is empty by whether or not the head node points to a node
    def Is_Empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    #Method that creates a Node object containing the input char. Then pushes that node onto the stack.
    def Push(self, char):
        temp = Node()
        temp.char = char
        temp.next = self.head_node
        self.head_node = temp
        # This functions first makes temp.next equal to whatever node
        # is at the head position. It then makes the new node the
        # head position, this implements LIFO ordering.

    #Method that pops nodes from the stack and returns the associated char
    def Pop(self):
        if(self.Is_Empty()):
            raise Exception("Stack is empty")
        else:
            temp = Node()
            temp = self.head_node
            self.head_node = self.head_node.next
            # Creates a new temp node which points to the head.
            # Then sets the head node to the following node
            # Finally, returns the temp node's data.
            return temp.char

    #A method that prints the entire contents of the stack, used for debugging purposes
    def Print_Stack(self):
        temp = self.head_node
        while(temp is not None):
            print(temp.char, end = " ")
            temp = temp.next
            # Prints the node's data, and then points to the following
            # Node. After the tail node temp will point to
            # None and the loop will break.

#The method that converts an expression from prefix to postfix
def Pre_To_Post(ThisString):
    x = len(ThisString)
    final = ""
    # x gets the length of the input expression for the loop range.
    # final represents the output string, but is also used for
    # combining terms to be pushed onto the stack.
    operandCount = 0
    operatorCount = 0
    # Operator and Operand counts for error checking
    NewStack = Stack()
    operators = ["+", "-", "*", "/", "$"]
    parenthesis = ["(", ")"]
    #Arrays containing operators and parenthesis for proper program
    #execution

    #NewStack creates a new Stack object. The operators array will be
    #used for comparison in the loop.


    firstChar = ThisString[0]
    if(firstChar not in operators):
        return "Error: Please ensure input is in Prefix notation"
    #This block ensures that the input is in prefix notation
    #by checking if an operator is the first character on the
    #left of the string.

    #Important note: This loop starts at the right side of the prefix
    #expression and iterates to the left.
    for i in range(x-1, -1, -1):
        if(ThisString[i].isnumeric()):
            #Simple catch statement to prevent use of numbers
            return "Error: Please do not use numbers"
        if(ThisString[i].isalpha()):
            NewStack.Push(ThisString[i])
            operandCount += 1
            # If the char is a letter, it is pushed to the stack
            #Operand count is incremented by 1
        elif(ThisString[i] in operators):
            try:
                operatorCount += 1
                final += NewStack.Pop()
                final += NewStack.Pop()
                final += ThisString[i]
                NewStack.Push(final)
                final = ""
                # If the char is an operator defined in the 'operators' list, two letters are
                # added to the string, followed by the operator. The string is then pushed back
                # on to the stack, and the "final" string is reset.
            except:
                #The try/except statement is meant to catch expressions
                #Where there are an incorrect number of operators.
                #If an operator is found and there are not enough
                #operands to support it the Pop() method will fail
                #and the loop breaks.
                return "Error: Invalid Expression (Too Many Operators)"
        elif(ThisString[i] == "^"):
            #A simple catch statement that asks the user to input
            #$ instead of ^.
            return "Error: Please use '$' to denote exponents"
        elif(ThisString[i] in parenthesis):
            #A simple catch statement that prevents the use
            #of parenthesis
            return ("Error: Order of Operations can be derived from prefix organization, please exclude parenthesis.")
    if(operandCount > operatorCount + 1):
        #Catch statement to prevent expressions with more operands
        #than the number of operators satisfies
        return "Error: Invalid Expression (Too Many Operands)"
    while(not NewStack.Is_Empty()):
        final = final + NewStack.Pop()
        # Pops entire stack to create final expression

    return final
    # Returns final expression

#The main function
def main():
    file_name = input("Please input the name of your file, including the extension: ")
    #Allows user input of file name to prevent
    #Hard coding file names
    try:
        with open(file_name, "r") as file:
            Lines = file.readlines()
            # Reads each line of the file into an array Lines
    except:
        print("Error reading file, please double check spelling.")
        return
        #The use of the try/except statement is meant to catch file
        #input errors
    with open("Output.txt", "w") as output:
        for line in Lines:
            line = line.replace(" ", "")
            #Removes whitespace in expressions
            line = line.strip()
            #Strips newline operators
            output.write(Pre_To_Post(line) + "\n")
            #Executes function while writing to a new file "output.txt"

#Call to the main function
main()
