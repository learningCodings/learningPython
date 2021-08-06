# Object Oriented In Python

class Point:
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

n = int(input("Enter Number: "))
n1 = int(input("Enter 2nd Number: "))

p = Point(n, n1)

print(f"The First Point Is: {p.x}")
print(f"The Second Point Is: {p.y}")