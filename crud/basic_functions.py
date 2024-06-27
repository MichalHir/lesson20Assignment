
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def search_index(cars_array):
    clear_terminal()
    print_all(cars_array)
    # model = input("what is the car model?")
    # brand = input("what is the car brand?")
    # color = input("what is the car color?")
    car_index = int(input("which car?")) -1
    # found=False
    # for index, car in enumerate(cars_array):
    #     if car["brand"] == brand and car["color"] == color and car["brand"] == brand:
    #         # found=True
    #         car_index = index
    return car_index

def search_print(cars_array):
    clear_terminal()
    search_str=""
    search_txt=str(input("What is the search term"))
    for index, car in enumerate(cars_array):
        if search_txt in car["model"] or search_txt.lower() in car["color"].lower  or search_txt.lower() in car["brand"].lower():
            found=True
            search_str +=f"{index+1} car model: {car["model"]} car brand: {car["brand"]} car color: {car["color"]}"
    if search_str=="":
        return print("no search results found")
    else:
        return search_str

def print_all(cars_array):
    clear_terminal()
    for index, car in enumerate (cars_array):
        print(index+1,car["model"],car["brand"],car["color"])


def add_car(cars_array):
    clear_terminal()
    # {"model": 2000, "brand": "kia", "color": "blue"}
    model = input("what is the car model you want to add?")
    brand = input("what is the car brand you want to add?")
    color = input("what is the car color you want to add?")
    new_car = {"model": model, "brand": brand, "color": color,"fav":False}
    cars_array.append(new_car)
    return print("that car has been added")


def edit_car(cars_array):
    clear_terminal()
    car_index = search_index(cars_array)
    if car_index != -1:
        new_model = input("what is the car model you want to add?")
        new_brand = input("what is the car brand you want to add?")
        new_color = input("what is the car color you want to add?")
        cars_array[car_index] = {
            "model": new_model,
            "brand": new_brand,
            "color": new_color,
        }
        return print("that car has been edited")
    else:
        return print("that car is not in the list")


def delete_car(cars_array):
    clear_terminal()
    car_index = search_index(cars_array)
    if car_index != -1:
        cars_array.pop(car_index)
        return print("that car has been deleted")
    else:
        return print("that car is not in the list")
