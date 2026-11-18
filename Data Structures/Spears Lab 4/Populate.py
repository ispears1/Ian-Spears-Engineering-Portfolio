import random as rd
#Imports the random python function to populate randomized files

#A function to populate files to be sorted
def Populate(num):
    #The extensions of the files I created
    in_order = str(num) + "_inOrder.txt"
    reverse_order = str(num) + "_reverseOrder.txt"
    random = str(num) + "_random.txt"

    #Writes the inorder file
    with open(in_order, "w") as file:
        for i in range(num):
            file.write(str(i))
            file.write("\n")

    #Writes the reverse order file
    with open(reverse_order, "w") as file:
        for i in range(num-1, -1, -1):
            file.write(str(i))
            file.write("\n")

    #Uses the inorder file to write the random order file, has no repeated numbers
    with open(in_order, "r") as file:
        numbers = file.readlines()
        for i in range(len(numbers)):
            numbers[i] = numbers[i].rstrip("\n")
            numbers[i] = int(numbers[i])
    with open(random, "w") as file:
        length = len(numbers)
        for i in range(length):
            random_index = rd.random() * len(numbers)
            random_index = int(random_index)
            random_number = numbers[random_index]
            numbers.pop(random_index)
            file.write(str(random_number))
            file.write("\n")

#A debugging function that resets the files of all sizes.
def repopulate():
    population_array = [50, 1000, 2000, 5000, 10000]
    for element in population_array:
        Populate(element)

