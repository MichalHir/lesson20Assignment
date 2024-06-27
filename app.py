from json_helper import read_json
from menu.main_menu import menu


def main():
    cars = read_json()
    menu(cars)


if __name__ == "__main__":
    main()
