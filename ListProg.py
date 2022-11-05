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
max = 99
OFFSETT = 4

genlist = [81,15,67,32,73,50,24,3,21,72]

# 'menu', creates the main menu to choose option or exit program
def list_menu():
    name = ' '*int(OFFSETT/2) + "Playing with Lists"
    dotted = (OFFSETT+len(name))*'-'
    options = ["[Reverse the List]", "[Add an element]", "[Delete an element]", "[Find the sum]", 
                "[Arrange in ascending order]", "[Arrange in descending order]", "[Exit]"]
    print('{} \n{} \n{}'.format(dotted, name, dotted))
    print("\nArray: ", genlist, "\n")
    print("What would you like to do with this list?")
    for i, opt in enumerate(options):
        print(i+1, opt)
    print(dotted)

# 'open_add_e', adds an element to the list
def open_add_e():
    while len(genlist) >= totalvalues:
        add = input("Input the number between {} and {} that you want to add to this list: ".format(min, max))
        try:
            add = int(add)
        except:
            print("Sorry, your input must be an integer!")
            continue
        if min <= add <= max:
            genlist.append(add)
            print("The number has been added!")
            print("\nYour New Array: ", genlist, "\n")
            main()
        else:
            print("Error! Your number was not in range")

# 'open_rev_l', reverses the order of the list
def open_rev_l():
    genlist.reverse()
    print("The list has been reversed!")
    print("\nYour New Array: ", genlist, "\n")
    main()

# 'open_del_e', deletes an element from the list
def open_del_e():
    while len(genlist) >= totalvalues:
        pickdel = input("Select the number you want to delete from the list: ")
        try:
            pickdel = int(pickdel) 
        except:
            print("Sorry, your input must be an integer!")
            continue
        if pickdel in genlist:
            genlist.remove(pickdel)
            print("The number has been deleted!")
            print("\nYour New Array: ", genlist, "\n")
            main()
        else:
            print("Error! Your number was not in the list!")
        
        
# 'open_sum_e', determines the sum of all the elements in the list
def open_sum_e():
    listsum = sum(genlist)
    print("\nThe sum of the values in the list is: ", listsum, "\n")
    print("\nYour New Array: ", genlist, "\n")
    main()

# 'open_asc_l', sorts the list in ascending order
def open_asc_l():
    genlist.sort()
    print("The list has been arranged in ascending order!")
    print("\nYour New Array: ", genlist, "\n")
    main()

# 'open_dsc_l', sorts the list in descending order
def open_dsc_l():
    genlist.sort()
    genlist.reverse()
    print("The list has been arranged in descending order!")
    print("\nYour New Array: ", genlist, "\n")
    main()

# 'main', calls the other functions
def main():
    list_menu()
    while True:
        choice = input("\nEnter your choice[1-7]: ")
        if choice == '1':
            string = '\n'"Reverse the List " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_rev_l()
            break

        elif choice == '2':
            string = '\n'"Add an element " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_add_e()
            break

        elif choice == '3':
            string = '\n'"Delete an element " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_del_e()
            break

        elif choice == '4':
            string = '\n'"Find the sum " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_sum_e()
            break

        elif choice == '5':
            string = '\n'"Arrange in ascending order " + "selected!"
            dotted = '\n'+ len(string) * "-"
            
            print(dotted,
                  string,
                  dotted)
            
            open_asc_l()
            break

        elif choice == '6':
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
        
main()