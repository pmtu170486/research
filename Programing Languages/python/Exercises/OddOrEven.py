## Exercise 2
## Ask the user for a number. Depending on whether the number is even or odd,
## print out an appropriate message to the user.
## Hint: how does an even / odd number react differently when divided by 2?
def solution():
    number = int(input("please enter number: "))
    if number%2==0:
        print("Number is even:",number)
    else:
        print("Number is odd:",number)
        
solution()