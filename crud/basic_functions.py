# print("write 1 if you want to print all of the cars")
#     print("write 2 if you want to add a car")
#     print("write 3 if you want to edit a car")
#     print("write 4 if you want to delete a car")
#     print("write 5 if you want to exit the menu")


def search_index(cars_array):
    print_all(cars_array)
    model = input("what is the car model you want to add?")
    brand = input("what is the car brand you want to add?")
    color = input("what is the car color you want to add?")
    car_index = -1
    # found=False
    for index, car in enumerate(cars_array):
        if car["brand"] == brand and car["color"] == color and car["brand"] == brand:
            # found=True
            car_index = index
    return car_index


def print_all(cars_array):
    for car in cars_array:
        print(car)


def add_car(cars_array):
    # {"model": 2000, "brand": "kia", "color": "blue"}
    model = input("what is the car model you want to add?")
    brand = input("what is the car brand you want to add?")
    color = input("what is the car color you want to add?")
    new_car = {"model": model, "brand": brand, "color": color}
    cars_array.append(new_car)
    return print("that car has been added")


def edit_car(cars_array):
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
    car_index = search_index(cars_array)
    if car_index != -1:
        cars_array.pop(car_index)
        return print("that car has been deleted")
    else:
        return print("that car is not in the list")
