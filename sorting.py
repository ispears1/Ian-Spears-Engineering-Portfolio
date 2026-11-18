# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:16:00 2019

@author: kwame
""" 

import random

def insertionSort(l):
    """
    This function sorts elements in l using insertion sort
    """
    steps = 0
    for i in range(1, len(l)):
        while l[i-1] > l[i] and i > 0:
            steps +=1
            l[i-1], l[i] = l[i], l[i-1]
            i -= 1
    return steps
    
def bubbleSort(l):
    steps = 0
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if(l[j]>l[j+1]):
                steps +=1
                l[j],l[j+1] = l[j+1], l[j]
    return steps

def selectionSort(l):
    steps = 0
    h = len(l)
    for i in range(len(l)):
        maximumIndex = 0
        for j in range(h):
            steps +=1
            if(l[j]>l[maximumIndex]):
                maximumIndex=j
        temp = l[j]
        l[j] = l[maximumIndex]
        l[maximumIndex] = temp
        steps +=3
        h = h-1
    return steps

if __name__ == "__main__":
    l = list(range(10)) # List of integers from 0 to 9

    random.shuffle(l)   # Shuffle list
    print("Unsorted:",l)    
    print("Insertion Steps:", insertionSort(l))
    print("Insertion Sorted:", l)
    
   
    random.shuffle(l)   
    print("\nUnsorted:",l)
    print("Bubble Steps:", bubbleSort(l))
    print("Bubble Sorted:", l)
    
    random.shuffle(l)
    print("\nUnsorted:",l)
    print("Selection Steps", selectionSort(l))
    print("Selection Sorted:", l)
    




