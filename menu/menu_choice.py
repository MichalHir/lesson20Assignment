from crud.basic_functions import add_car, delete_car, edit_car, print_all, search_print
from crud.favourites import add_to_favorites, print_favorites, remove_from_favorites
from json_helper import save_json


def choose(cars_array, selection):
    if selection == "1":
        print_all(cars_array)
    if selection == "2":
        add_car(cars_array)
        save_json(cars_array)
    if selection == "3":
        edit_car(cars_array)
        save_json(cars_array)
    if selection == "4":
        delete_car(cars_array)
        save_json(cars_array)
    if selection == "5":
        search_txt = search_print(cars_array)
        if search_txt!="":
            print(search_txt)
    if selection == "6":
        add_to_favorites(cars_array)
        save_json(cars_array)
    if selection == "7":
        remove_from_favorites(cars_array)
        save_json(cars_array)
    if selection == "8":
        fav_txt = print_favorites(cars_array)
        print(fav_txt)
    if selection == "9":
        save_json(cars_array)
