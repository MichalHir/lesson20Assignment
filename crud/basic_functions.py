
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
def if_empty(cars_array):
    if len(cars_array) == 0:
        return True
    else:
        return False
def search_index(cars_array):
    clear_terminal()
    print_all(cars_array)
    car_index = int(input("which car?\n in case you dont find that car write 11 to return to menu\n")) -1
    return car_index

def search_print(cars_array):
    clear_terminal()
    search_str=""
    search_txt=str(input("What is the search term"))
    for index, car in enumerate(cars_array):
        if search_txt in str(car["model"]) or search_txt.lower() in car["color"].lower()  or search_txt.lower() in car["brand"].lower():
            found=True
            search_str +=f"{index+1} car model: {car["model"]} car brand: {car["brand"]} car color: {car["color"]}\n"
    if search_str=="":
        return print("no search results found")
    else:
        return search_str

def print_all(cars_array):
    clear_terminal()
    if if_empty(cars_array):
        return print("no cars to print, back to menu")
    for index, car in enumerate (cars_array):
        print(index+1,car["model"],car["brand"],car["color"])


def add_car(cars_array):
    clear_terminal()
    model = input("what is the car model you want to add?\n")
    brand = input("what is the car brand you want to add?\n")
    color = input("what is the car color you want to add?\n")
    new_car = {"model": model, "brand": brand, "color": color,"fav":False}
    cars_array.append(new_car)
    return print("that car has been added")


def edit_car(cars_array):
    clear_terminal()
    if if_empty(cars_array):
        return print("no cars in the garage, back to menu")
    car_index = search_index(cars_array)
    if car_index != 10:
        new_model = input("what is the new car model?\n")
        new_brand = input("what is the new car brand?\n")
        new_color = input("what is the new car color?\n")
        cars_array[car_index] = {
            "model": new_model,
            "brand": new_brand,
            "color": new_color,
        }
        return print("that car has been edited")
    else:
        return print("that car is not in the list, back to menu")


def delete_car(cars_array):
    clear_terminal()
    if if_empty(cars_array):
        return print("no cars in the garage, back to menu")
    car_index = search_index(cars_array)
    if car_index != 10:
        cars_array.pop(car_index)
        return print("that car has been deleted")
    else:
        return print("that car is not in the list, back to menu")
