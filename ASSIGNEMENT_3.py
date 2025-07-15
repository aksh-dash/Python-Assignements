## ASSIGNEMENT_3.1# This program calculates the factorial of a number using recursion

n= int(input("Enter a number: "))

def factorial(n):
    if n < 2 :
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(n)
print("Factorial of", n, "is", result)


##ASSIGNMENT_3.2# CALCULATION
import math as m
 
n= input ("Enter a number: ")
print("Square root of", n, "is", m.sqrt(int(n)))
print("Logarithm of", n, "is", m.log(int(n)))
print("sine of", n, "is", m.sin(int(n)))