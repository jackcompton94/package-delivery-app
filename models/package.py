# Jack Compton
# C950 - DSA II
# April 7th, 2023

from data_structures import chaining_hash_table
import csv

package_hash = chaining_hash_table.ChainingHashTable()


class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, kilo, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes
        # base delivery status is at the hub, this is updated when departing or delivered
        self.delivery_status = "at the hub"
        # delivery_time is set once package arrives to location
        self.delivery_time = None
        self.departure_time = None
        self.truck_id = ""

    def __str__(self):
        return f"Package ID: {self.package_id} | Full Address: {self.address} {self.city},{self.state} {self.zip} | Deadline: {self.deadline} | Kilo: {self.kilo} | Delivery Status: {self.delivery_status} | Delivery Time: {self.delivery_time} | Departure Time: {self.departure_time} | Truck ID: {self.truck_id}"


def load_package_data(file):
    # Opens file to read into memory
    with open(file) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)
        # Extract CSV data into variables to create package objects
        for row in package_data:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            deadline = row[5]
            kilo = row[6]
            notes = row[7]

            # Instantiates objects per package and inserts into the chaining hash table
            p = Package(package_id, address, city, state, zip, deadline, kilo, notes)
            package_hash.insert(package_id, p)
