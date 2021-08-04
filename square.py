# importing my function

# from mathsFunctions import square
from mathsFunctions import *
n = float(input("Enter Any Number: "))

n = square(n)

print(f"The Squre Is: {n}")

# I want print square of 0 to 100 numbers

for i in range(101):
    print(f"The Squre Of{i} Is: {square(i)}\n")