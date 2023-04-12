# Jack Compton
# Student ID: 001511804
# C950 - DSA II
# April 7th, 2023

import datetime
import menu
from datetime import timedelta
from models import package, truck, distance
from algorithms import route_planner, truck_load_planner

PACKAGE_CSV = 'csvs/WGUPS Package File.csv'
DISTANCE_CSV = 'csvs/WGUPS Distance Table.csv'

# converts CSV to Package objects stored in a hash table
package.load_package_data(PACKAGE_CSV)

# converts CSV and cleans the data for usability throughout program
distance.load_distance_data(DISTANCE_CSV)

# Initializing the three trucks owned by WGUPS
truck_one = truck.Truck(1, timedelta(hours=8, minutes=0))
truck_two = truck.Truck(2, timedelta(hours=9, minutes=5))
truck_three = truck.Truck(3, timedelta(hours=10, minutes=0))

# Loading the three trucks
truck_load_planner.load_trucks(truck_one, truck_two, truck_three)

# Using the loaded trucks, plan the route they will take for the day
route_planner.plan_route()

# Generate Menu
menu.main_menu()
