# Flight Seats 

class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    # def booked_seats(self):
    #     return 

seats =int(input("Enter Number Of Seats In Flight: "))
flight = Flight(seats)


people = []
f = int(input("Enter Number Of Passengers To Book Flight: "))

for i in range(0, f):
    person = input("Enter Person Name: ")
    people.append(person)

print(f"\nThe Peoples Are Added: {people}\n")

# people = ["Tony", "Thor", "Loki"]
for persons in people:
    success = flight.add_passenger(persons)
    if success:
        print(f"Booked {persons} In Flight Successfully")
    else:
        print("\n")
        print(f"Not Seat Available For {persons}")