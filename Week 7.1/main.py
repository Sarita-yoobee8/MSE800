# impport fish_factory and database
#design pattern used------- factory pattern 

from fish_factory import FishFactory
from database import add_fish_to_db, view_inventory


def add_fish():

    print("\nAvailable Fish:")
    print("Goldfish")
    print("Shark")
    print("Angelfish")
    print("Tuna")
    print("Salmon")

    fish_name = input("Enter fish type: ")

    # Factory creates object
    fish = FishFactory.create_fish(fish_name)

    if fish:

        # Store in database
        add_fish_to_db(fish.get_category())

        print(f"{fish.get_category()} added successfully!")

    else:
        print("Invalid fish type.")


# Main Program
while True:

    print("\n===== AUCKLAND AQUARIUM =====")
    print("1. Add Fish")
    print("2. View Aquarium")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_fish()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        print("System is shutting down")
        break

    else:
        print("Please enter valid data")