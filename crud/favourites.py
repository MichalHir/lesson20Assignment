from crud.basic_functions import clear_terminal, search_index


def print_not_favorites(cars_array):
    clear_terminal()
    search_str="" 
    for index, car in enumerate (cars_array):
        if car["fav"]==False:
            search_str +=f"{index+1} car model: {car["model"]} car brand: {car["brand"]} car color: {car["color"]}\n"
    return search_str


def add_to_favorites(cars_array):
    clear_terminal()
    not_favourites_txt=print_not_favorites(cars_array)
    if not_favourites_txt=="":
        return print("there are no cars to add to favorites, back to menu")
    print(not_favourites_txt)
    fav_index= int(input("which car?\n in case you dont find that car write 11 to return to menu\n")) -1
    if fav_index==10 :
        return print("back to menu")
    else:
        cars_array[fav_index]["fav"]=True
        return print("that car has been favorited")
    

def remove_from_favorites(cars_array):
    clear_terminal()
    favourites_txt=print_favorites(cars_array)
    if favourites_txt=="":
        return print("there are no cars to remove from favorites, back to menu")
    print(favourites_txt)
    fav_index=int(input("which car?\n in case you dont find that car write 11 to return to menu\n")) -1
    if fav_index==10:
        return print("back to menu")
    else:
        cars_array[fav_index]["fav"]=False
        return print("that car has been removed from favorited")
    

def print_favorites(cars_array):
    clear_terminal()
    search_str="" 
    for index, car in enumerate (cars_array):
        if car["fav"]==True:
            search_str +=f"{index+1} car model: {car["model"]} car brand: {car["brand"]} car color: {car["color"]}\n"
    if search_str=="":
        search_str="there are no favorites"
    return search_str
