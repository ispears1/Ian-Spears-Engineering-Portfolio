operators = ["+", "-", "*", "/", "$"]
#An array containing all acceptable operators
#It is included in this file since it needs to be accessed here and in main(), and all
#elements of this file are imported to main()

def PreToPostRecursive(expression):
    if(expression == ""):
        return ""
    #If the expression is empty, the program returns nothing
    if(expression[0].isalpha()):
        return expression[0]
    #If the first letter of the expression is a letter, the program returns that letter
    elif(expression[0] in operators):
        operator = expression[0]
        operand1 = PreToPostRecursive(expression[1:])
        m = len(operand1)
        operand2 = PreToPostRecursive(expression[m+1:])
        return operand1 + operand2 + operator
    #If the first letter of the expression is an operator, then operand1 is defined as the next character, and operand2 is defined
    #as the expression substring from after operand1 to the end of the expression. Operand1 and operand2 are rewritten in postfix by
    #a recursive function call, and then the operator, operand1, and operand2 are rewritten in postfix.