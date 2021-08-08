# lambda Use

# in python we can define dict under list or dict under dict

people = [
    
    {"name" : "RDJ", "charcter" : "Tony"},
    {"name" : "Chris H", "charcter" : "Thor"},
    {"name" : "Tom H", "charcter": "Loki"}
]

print(f"\nThe List Is: {people}")

# python can not sort dict to dict I need to define function to sort it
"""def f(person):
    return person["name"]"""

# to avoid use of this own defined code instead of it I can use lambda

people.sort(key = lambda person: person["charcter"] )

print(f"\n{people}")