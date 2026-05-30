# Parent Class
class general_flight:
    def __init__(self, flight_number, origin, destination, arrival_time, departure_time):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.arrival_time = arrival_time
        self.departure_time = departure_time

    def display_flight(self):
        print("Flight Number:", self.flight_number)
        print("Origin:", self.origin)
        print("Destination:", self.destination)
        print("Arrival Time:", self.arrival_time)
        print("Departure Time:", self.departure_time)


# Child Class (Single Inheritance)
class domestic_flight(general_flight):
    def __init__(self, flight_number, origin, destination, arrival_time, departure_time, baggage_allowance):
        super().__init__(flight_number, origin, destination, arrival_time, departure_time)
        self.baggage_allowance = baggage_allowance

    def display_baggage(self):
        print("Baggage Allowance:", self.baggage_allowance, "kg")


# Create object
f1 = domestic_flight(
    "NZ123",
    "Auckland",
    "Wellington",
    "09:10 AM",
    "08:00 AM",
    23
)

# Call parent method
f1.display_flight()

print("-----")

# Call child method
f1.display_baggage()