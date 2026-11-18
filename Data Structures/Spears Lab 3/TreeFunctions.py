#A python file containing the Tree class and its associated functions.
class Tree():

    def __init__(self, letter, frequency):
        # A tree must be defined with a letter and that letter's frequency. It's default left and right pointers
        # point to None
        self.letter = letter
        self.frequency = frequency
        self.left = None
        self.right = None


    def setLeft(self, Node):
        # A function that sets the left pointer of a tree. If that left pointer is already pointing to another tree, it recursively calls
        # the function to the tree at that left pointer.
        if(self.left != None):
            self.left.setLeft(Node)
        else:
            self.left = Node


    def setRight(self, Node):
        # A function that sets the right pointer of a tree. If that right pointer is already pointing to another tree, it recursively calls
        # the function to the tree at that right pointer.
        if(self.right != None):
            self.right.setRight(Node)
        else:
            self.right = Node


    def printTree(self):
        #A debugging function that prints the tree in inorder fashion
        if(self.left != None):
            self.left.printTree()
        print(self.letter)
        print(self.frequency)
        print(self.code)
        if(self.right != None):
            self.right.printTree()


