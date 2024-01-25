import Utilities

def edit_recipe_menu():
    
    

    while True:
        print("Enter one of the following options: ")
        choice = inp_no_range()

        if choice == 1:
            print("1 was picked")
        elif choice == 2:
            print("2 was pciked")
        elif choice == 3:
            print("3 was picked")
        elif choice == 4:
            print("4 was picked")
        elif choice == 5:
            print("5 was picked")
        elif choice == 6:
            print()
        elif choice == 7:
            print()
        elif choice == 8:
            break

def menu():
    while True:
        print("Enter one of the following options:\n1: List all Recipes\n2: Open Recipe\n 3: Add New Recipe\n4: Remove Recipe\n5: Edit Recipe\n6: Quit")
        choice = inp_no_range(choice)

        if choice == 1:
            print("1 was picked")
        elif choice == 2:
            print("2 was pciked")
        elif choice == 3:
            print("3 was picked")
        elif choice == 4:
            print("4 was picked")
        elif choice == 5:
            print("5 was picked")
        elif choice == 6:
            print("GOOD BYE!")
            break

menu()