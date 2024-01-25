class Recipe:
    def __init__(self, name, no_ingredients, ingredients, no_processes, proccesses, description, time_make, rate):
        self.name = name
        self.no_ingredients = no_ingredients
        self.ingredients = ingredients
        self.no_processes = no_processes
        self.proccesses = proccesses
        self.description = description
        self.time_make = time_make
        self.rate = rate

def show_name():
    return self.name