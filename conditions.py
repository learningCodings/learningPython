#conditions if elif else

print("Working Of 'if else'")

#If I want To Take input as number then I've to specify before input
n = float(input("Enter Number: "))

if n > 0:
    print(f"{n} Is Positive")
elif n < 0:
    print(f"{n} Is Negative")
else:
    print(f"{n} Is Zero")