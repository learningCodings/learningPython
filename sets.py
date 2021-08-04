# sets in Python

# declare set

s = set()

# add elements in set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(7)

print(s)

# Add 7 again in set

s.add(7)

print(s)


""" In Maths Set Dose Allow Repated Data In It Follows As It Is 
So Set Contain Only Unique Data """
 

# remove 3 from set

s.remove(3)
print(s)

# Find length of set

print(f"{s} Has Toatl: {len(s)} Elements")