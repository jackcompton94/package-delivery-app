# Jack Compton
# C950 - DSA II
# April 8th, 2023

import csv
from _datetime import timedelta

distances = []


# reads distance CSV into memory (2D Array)
def load_distance_data(file):
    with open(file) as distance_file:
        distance_data = csv.reader(distance_file, delimiter=',')
        for row in distance_data:
            # cleans data for use later in the program
            new_row = [row[0].replace('\n', ' ').replace('  ', ' ')] + [header.replace('\n', ' ').replace('  ', ' ') for header in row[1:]]
            distances.append(new_row)


# function to get the distance between two addresses
def get_distance(address_1, address_2):
    row_index = None
    for i, row in enumerate(distances):
        if row[0] == address_1:
            row_index = i
            break

    col_index = None
    for i, address in enumerate(distances[0]):
        if address == address_2:
            col_index = i
            break

    # Gets the distance value set in the CSV using the row and column indices
    distance_in_miles = distances[row_index][col_index]

    # Checks if the value is null, if so reverse the indices to get the distance value
    if not bool(distance_in_miles):
        distance_in_miles = distances[col_index][row_index]

    return distance_in_miles


# Time Complexity -> O(n)
# Space Complexity -> O(1)
def get_route_data(truck):
    left = 0
    right = 1

    while right < len(truck.route):
        truck.mileage += float(get_distance(truck.route[left], truck.route[right]))
        left += 1
        right += 1

        # time = distance / speed
        travel_time = timedelta(hours=truck.mileage/truck.speed)
        delivery_time = truck.departure_time + travel_time

        # Sets the delivery_time for each package
        for i in range(len(truck.packages)):
            if truck.packages[i].address in truck.route[left]:
                truck.packages[i].delivery_time = delivery_time
                # Delivers the package, thus removes it from the truck
                del truck.packages[i]
                break
