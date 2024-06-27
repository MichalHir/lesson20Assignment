from json_helper import read_json
from menu.menu_choice import choose


def menu():
    while True:
        cars_array = read_json()
        print("welcome to the garage")
        print("write 1 if you want to print all of the cars")
        print("write 2 if you want to add a car")
        print("write 3 if you want to edit a car")
        print("write 4 if you want to delete a car")
        print("write 5 if you want to search the list")
        print("write 6 if you want to mark a car as favourite")
        print("write 7 if you want to remove a car from favourite")
        print("write 8 if you want to print all of the favourite cars")
        print("write 9 if you want to exit the menu")
        choice = input("enter your choice\n")
        choose(cars_array, choice)
        if choice == "9":
            print("goodbye")
            break
