#question 06


def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)

n = int(input("Enter a positive integer number: "))
print("The factoral of 5 is", factorial(n))