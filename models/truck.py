# Jack Compton
# C950 - DSA II
# April 7th, 2023

MAX_CAPACITY = 16
TRUCK_SPEED = 18
truck_fleet = []


class Truck:
    def __init__(self, truck_id, departure_time):
        self.truck_id = truck_id
        self.speed = TRUCK_SPEED
        self.packages = []
        self.route = []
        self.departure_time = departure_time
        self.mileage = 0

    def add_packages(self, package):
        if len(self.packages) < MAX_CAPACITY:
            if bool(package):
                self.packages.append(package)
        else:
            print("Unable to load package, truck is at capacity")

    def add_to_route(self, next_loc):
        self.route.append(next_loc)

    def __str__(self):
        return f"Truck ID: {self.truck_id} | Mileage: {self.mileage} | Departure Time: {self.departure_time}"
