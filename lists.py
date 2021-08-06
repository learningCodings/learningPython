# Get Inputs To List From User

lst = []

num = int(input("Enter Number Of Elements: "))

for i in range(0, num):
    name = input("Enter Names: ")
    lst.append(name)

print(f"The Names Added In List Are: {lst}")

# List Data Structure

names = ["Tony", "Flash", "Thor", "Loki", "Chris"]

print(names)

# Print Perticular Name Thor

print(names[2])

# Add Natasha At End Of The List

names.append("Natasha")
print(names)

# Sort This List 

names.sort()
print(names)

#sort this list in decendig order

names.sort(reverse = True)
print(f"Reverse List: {names}")

