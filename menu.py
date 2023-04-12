import datetime

import re
from models import package, truck


def main_menu():
    while True:
        print("\n==== Welcome to WGUPS Simulation ====")
        print("1. View a package")
        print("2. View a package at a specific time")
        print("3. View trucks and total mileage")
        print("4. View ALL packages at a specific time")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            package_id = input("Enter the package ID: ")
            view_package_details(package_id)
        elif choice == "2":
            package_id = input("Enter the package ID: ")
            time = input("Enter the time (HH:MM): ")
            view_a_package_at_time(package_id, time)
        elif choice == "3":
            view_truck_data(truck)
        elif choice == "4":
            time = input("Enter the time (HH:MM): ")
            view_all_packages_at_time(time)
        elif choice == "5":
            print("Closing")
            break
        else:
            print("Invalid choice, please try again.")


def view_package_details(package_id):
    try:
        package_id = int(package_id)
        if package_id < 1 or package_id > 40:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 40.")
        return

    print(f"\n==== Package Details for Package {package_id} ====")
    p = package.package_hash.search(int(package_id))
    print(p)


def view_truck_data(truck):
    print(f"\n==== Truck Data ====")
    total_mileage = 0
    for i in range(len(truck.truck_fleet)):
        print(truck.truck_fleet[i])
        total_mileage += truck.truck_fleet[i].mileage
    print(f"Total mileage: {total_mileage}")


def view_all_packages_at_time(user_time):
    if not isinstance(user_time, str) or not re.match(r"\d{2}:\d{2}", user_time):
        print("Invalid time format. Please enter time in HH:MM format.")
        return

    try:
        time_parts = user_time.split(":")
        time_delta = datetime.timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]))
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")
        return

    print(f"\n==== Packages at {user_time} ====")

    for package_id in range(1, 41):
        p = package.package_hash.search(package_id)
        if time_delta < p.departure_time:
            p.delivery_status = "at the hub"
        elif time_delta < p.delivery_time:
            p.delivery_status = "en route"
        else:
            p.delivery_status = f"delivered at {p.delivery_time}"
        print(p)


def view_a_package_at_time(package_id, user_time):
    try:
        package_id = int(package_id)
        if package_id < 1 or package_id > 40:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 40.")
        return

    if not isinstance(user_time, str) or not re.match(r"\d{2}:\d{2}", user_time):
        print("Invalid time format. Please enter time in HH:MM format.")
        return

    try:
        time_parts = user_time.split(":")
        time_delta = datetime.timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]))
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")
        return

    p = package.package_hash.search(package_id)
    if time_delta < p.departure_time:
        p.delivery_status = "at the hub"
    elif time_delta < p.delivery_time:
        p.delivery_status = "en route"
    else:
        p.delivery_status = f"delivered at {p.delivery_time}"
    view_package_details(package_id)


if __name__ == '__main__':
    main_menu()
