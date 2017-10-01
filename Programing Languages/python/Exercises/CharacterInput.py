# http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
# Exercise 1
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime
def solution():
    name = input("Please enter name: ")
    age = int(input("Please enter age: "))
    current = datetime.now().year
    result = (current + 100) - age
    print("Name: " + name)
    print("To year "+ str(result) + ", you will 100 year old")
    
solution()
