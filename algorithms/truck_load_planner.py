# Jack Compton
# C950 - DSA II
# April 10th, 2023

from models import truck, package


# Manually load trucks per package specifications
def load_trucks(truck_one, truck_two, truck_three):
    truck_one.packages = [
        package.package_hash.search(1),
        package.package_hash.search(8),
        package.package_hash.search(13),
        package.package_hash.search(14),
        package.package_hash.search(15),
        package.package_hash.search(16),
        package.package_hash.search(19),
        package.package_hash.search(20),
        package.package_hash.search(21),
        package.package_hash.search(29),
        package.package_hash.search(30),
        package.package_hash.search(31),
        package.package_hash.search(34),
        package.package_hash.search(37),
        package.package_hash.search(39),
        package.package_hash.search(40)
    ]
    truck_two.packages = [
        package.package_hash.search(3),
        package.package_hash.search(4),
        package.package_hash.search(5),
        package.package_hash.search(6),
        package.package_hash.search(7),
        package.package_hash.search(9),
        package.package_hash.search(17),
        package.package_hash.search(18),
        package.package_hash.search(25),
        package.package_hash.search(26),
        package.package_hash.search(28),
        package.package_hash.search(32),
        package.package_hash.search(36),
        package.package_hash.search(38)
    ]
    truck_three.packages = [
        package.package_hash.search(2),
        package.package_hash.search(10),
        package.package_hash.search(11),
        package.package_hash.search(12),
        package.package_hash.search(22),
        package.package_hash.search(23),
        package.package_hash.search(24),
        package.package_hash.search(27),
        package.package_hash.search(33),
        package.package_hash.search(35),
    ]

    # Assigns each package the trucks departure time and truck ID
    for t in range(len(truck_one.packages)):
        truck_one.packages[t].departure_time = truck_one.departure_time
        truck_one.packages[t].truck_id = truck_one.truck_id

    for t in range(len(truck_two.packages)):
        truck_two.packages[t].departure_time = truck_two.departure_time
        truck_two.packages[t].truck_id = truck_two.truck_id

    for t in range(len(truck_three.packages)):
        truck_three.packages[t].departure_time = truck_three.departure_time
        truck_three.packages[t].truck_id = truck_three.truck_id

    # Adds truck to the fleet for the day
    truck.truck_fleet.append(truck_one)
    truck.truck_fleet.append(truck_two)
    truck.truck_fleet.append(truck_three)
