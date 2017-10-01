##Exercise 3
##Take a list, say for example this one:
##
##  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##  
##and write a program that prints out all the elements of the list that are less than 5.
from random import randint
def createList():
    list = []
    i=0
    while i < 10:
        element = randint(0,20)
        list.append(element)
        i=i+1
    return list
    

def solution():
    list = createList()
    for value in list:
        if value < 10 and value>0:
            print("\nElement less than 5: ",value)

solution()
    