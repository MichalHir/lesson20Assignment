from crud.basic_functions import clear_terminal, search_index


def add_to_favorites(cars_array):
    clear_terminal()
    fav_index=search_index(cars_array)
    cars_array[fav_index]["fav"]=True
    print("that car has been favorited")

def remove_from_favorites(cars_array):
    clear_terminal()
    print_favorites(cars_array)
    fav_index=search_index(cars_array)
    cars_array[fav_index]["fav"]=False
    print("that car has been removed from favorited")

def print_favorites(cars_array):
    clear_terminal()
    for index, car in enumerate (cars_array):
        if car["fav"]==True:
            print(index+1,car["model"],car["brand"],car["color"])
