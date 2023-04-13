from models import truck, distance


# Time Complexity -> O(n^3)
# Space Complexity -> O(1)
def plan_route():

    # Loops through truck_fleet
    for i in range(len(truck.truck_fleet)):
        # Sets the hub as the first address in the route
        truck.truck_fleet[i].route.append(distance.distances[1][0])

        # Loops through all packages loaded on truck
        for p in range(len(truck.truck_fleet[i].packages)):

            # Loops through the distance CSV to find the matching addresses for distance value
            for d in range(len(distance.distances)):
                # If the package address string is in the distance CSV string set the next location to the trucks route and break out of the loop
                if truck.truck_fleet[i].packages[p].address in distance.distances[d][0]:
                    next_loc = distance.distances[d][0]
                    truck.truck_fleet[i].route.append(next_loc)
                    break

        # Gets minimum distances for each package in route
        optimize_route(truck.truck_fleet[i].route)

        # Gets and Prints the total distance traveled for the fleet of trucks
        distance.get_route_data(truck.truck_fleet[i])


# Time Complexity -> O(n^2)
# Space Complexity -> O(1)
# Nearest Neighbor Algorithm
def optimize_route(truck_route):
    for i in range(len(truck_route)-1):
        # Set minimum distance to the distance between the current and next stop
        min_distance = float(distance.get_distance(truck_route[i], truck_route[i+1]))
        # Set index of the minimum distance to the next stop
        min_index = i+1
        # Loops through all stops in the route after current stop
        for j in range(i+1, len(truck_route)):
            # Calculate the distance between the current stop and the next stop
            check_distance = float(distance.get_distance(truck_route[i], truck_route[j]))
            # If the distance between the current stop and the next stop being checked is smaller than the minimum distance,
            # set the minimum distance to the check distance and update the index of the minimum distance
            if check_distance < min_distance:
                min_distance = check_distance
                min_index = j
        # If the index of the minimum distance is not the next stop in the truck route,
        # swap the location of the next delivery based on the minimum distance from the current stop
        if min_index != i+1:
            # Swaps the location of the next delivery based on the minimum distance from the current stop
            truck_route[i+1], truck_route[min_index] = truck_route[min_index], truck_route[i+1]
    return truck_route

