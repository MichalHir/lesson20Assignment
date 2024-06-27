from crud.basic_functions import add_car, delete_car, edit_car, print_all
from json_helper import save_json


def choose(cars_array, election):
    if election == "1":
        print_all(cars_array)
    if election == "2":
        add_car(cars_array)
    if election == "3":
        edit_car(cars_array)
    if election == "4":
        delete_car(cars_array)
    if election == "5":
        save_json(cars_array)
