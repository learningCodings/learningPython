# To define function I've tO use def keyword 

def square(x):
    return x * x
    
def add(x,y):
    return x + y

n  = int(input("Enter Number: "))
n1 = int(input("Enter Number: "))

n = square(n)
n1 = add(n, n1)

print(f"The Square Is: {n}")
print(f"The Addition Is: {n1}")