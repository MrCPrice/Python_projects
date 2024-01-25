from Recipes import Recipe

def inp_no_menu():
    options = [1, 2, 3, 4, 5, 6]
    user_input = input("Enter: ")[0]

    if not user_input.__contains__(options):
        print("ERROR must enter only one folling options: " + options)
    else:
        return user_input

def inp_no_sup_menu():
    options = [1, 2, 3, 4, 5, 6, 7, 8]
    user_input = input("Enter: ")[0]

    if not user_input.__contains__(options):
        print("ERROR must enter only one folling options: " + options)
    else:
        return user_input

def import_recipes(recipe_file):
    array = []
    for recipe in recipe_file:
        array.append(Recipe(recipe.removesuffix("\n")))
    return array

file_name = "C:\\Users\\conno\\Coding projects\Python\\Recipe Book App\\Recipe_Book.txt" 
recipes = import_recipes(open(file_name, "r"))

def show_all_recipes():
    no = 0
    for recipe in recipes:
        print("ID: " + no + " Name: " + Recipe(recipe).show_name)
        no += 1

def pick_recipe():
    print()

def add_recipe():
    print("Creating Recipe")

def removing_recipe():
    print("Removing Recipe")

def edit_recipe_menu():
    print()