# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

# Example Output:

# Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
# Menu:
#  1 -> Add an element
#  2 -> Insert an element
#  3 -> Modify an element
#  4 -> Delete an element
#  5 -> Arrange in ascending order
#  6 -> Arrange in descending order
# What do you want to do? (1-6): 4
# Enter the index you want to delete: 3
# The element has been deleted
# This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]

import random
totalvalues = 10
min = 0
max = 999
OFFSETT = 4

# 'menu', creates the main menu to choose option or exit program

def get_list_values():
    return sorted(random.sample(range(min, max), totalvalues)) 

def list_menu():
    name = ' '*int(OFFSETT/2) + "Playing with Lists"
    dotted = (OFFSETT+len(name))*'-'
    genlist = get_list_values()
    options = ["[Add an element]", "[Insert an element]", "[Modify an element]", "[Delete an element]", 
                "[Arrange in ascending order]", "[Arrange in descending order]", "[Exit]"]
    print('{} \n{} \n{}'.format(dotted, name, dotted))
    print("\nArray: ", genlist, "\n")
    print("What would you like to do with this list?")
    for i, opt in enumerate(options):
        print(i+1, opt)
    print(dotted)

def main():
    list_menu()
    while True:
        choice = input("\nEnter your choice[1-7]: ")
        if choice == '1':
            string = '\n'"Add an element " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_add_e()
            break

        if choice == '2':
            string = '\n'"Insert an element " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_ins_e()
            break

        if choice == '3':
            string = '\n'"Modify an element" + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_mod_e()
            break

        if choice == '4':
            string = '\n'"Delete an element " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_del_e()
            break

        if choice == '5':
            string = '\n'"Arrange in ascending order " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_asc_l()
            break

        if choice == '6':
            string = '\n'"Arrange in descending order " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_dsc_l()
            break

        elif choice == '7':
            print ("Thanks for playing!\n")
            break
                         
        print("Error! Invalid input. Press any key to continue...\n")
        
if __name__ == '__main__':
    main()