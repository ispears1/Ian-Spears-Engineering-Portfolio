from PreToPostRecursive import *
#Import statement to obtain functions and arrays from PreToPostRecursive.py
parenthesis = ["(", ")"]
#Array containing parenthesis characters, used for error checking later

#The main function
def main():
    try:
        fileName = input("Enter file name, including extension: ")
        with open(fileName, "r") as InputVals:
            Lines = InputVals.readlines()
    except:
        print("Error: Invalid File Name")
        return
    #Try/except statement that accepts the users input for a file name
    with open("output.txt", "w") as OutputVals:
        #Opens or creates 'output.txt'
        for line in Lines:
            line = line.strip()
            line = line.replace(" ", "")
            #These statements remove all the whitespace from expressions
            if(line == ""):
                continue
                #This if statement skips empty file lines
            if(line[0].isalpha()):
                OutputVals.write("Error: Please ensure expression is in prefix notation.\n")
                continue
                #This error checking statement ensures the expression is not written in postfix or infix
            if(any(character.isdigit() for character in line)):
                OutputVals.write("Error: Please do not use digits.\n")
                continue
                #This error checking statement checks for digits
            if(any(character in parenthesis for character in line)):
                OutputVals.write("Error: Prefix notation can be used to determine order of operations; please exclude parenthesis.\n")
                continue
                #This error checking statement checks for parenthesis (see array above)
            if(any(character == "^" for character in line)):
                OutputVals.write("Error: Please use '$' instead of '^'.\n")
                continue
                #This error checking statement ensures the expression does not contain '^' instead of '$'
            operator_count = 0
            operand_count = 0
            for letter in line:
                if (letter in operators):
                    operator_count += 1
                elif (letter.isalpha()):
                    operand_count += 1
            if (operator_count != operand_count - 1):
                OutputVals.write("Error: Improper statement. Please check number of operands and operators.\n")
                continue
            #This for loop/if statement combination ensures that the expression has an appropriate number of operators
            #and operands
            OutputVals.write(PreToPostRecursive(line))
            OutputVals.write("\n")
            #If the expression passes all these checks, it is run through PreToPostRecursive(), written to
            #The output file, and then a newline is written to the file

main()
#Calls the main function