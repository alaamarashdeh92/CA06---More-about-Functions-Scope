# Shopping List

# Your shopping list should keep asking for new items until nothing is entered (no input followed by enter/return key).
# The program should then print a menu for the user to choose one of the following options:
# (A)dd - To add a new item to the list.
# (F)ind - To search for an item in the list.
# (P)rint - To pretty print the list.
# (S)ort - To sort the list.
# (C)lear - To clear all items in the list.
# (Q)uit - To exit your program.

# TODO: Define a data structure to keep track of your shopping list.

# TODO: Implement a function to show the menu to the user, then wait for a valid user choice.
def add_item(item):
    shopping_list.append(item)

#Implement a function to find an item in your shopping list.
def find_item(item):
    if item in shopping_list:
        print("the item was found ")
    else:
        print("the items is not in the list ")

#implement a function to pretty print your tabbed lits.

def print_list():
    print("the items in the list are ")
    print(shopping_list, end ="/t")

# function to sort print your tabbed lits.

def sort_list():
    shopping_list.sort()
    print (f"the sorted shopping list is {shopping_list}")

#Implement a function to pretty print your tabbed lits.
def clear_list():
    shopping_list.clear()

#Implement a function which calls the exit() function.
def quit():
    print("Goodbye! Hope to see you again soon :).")
 

shopping_list=[]

def show_menu():
 print(f"this is the menu{shopping_list}")
 print ("""chose one of the following options
 Add - To add a new item to the list.
 Find - To search for an item in the list.
 Print - To pretty print the list.
 Sort - To sort the list.
 Clear - To clear all items in the list.
 Quit - To exit your program.
 
 """)
str=input("your choice is :")
if str=="Add" :
    item=input("enter the item you want to add ")
    add_item(item)
 
elif str=="find":
    item=input("what are you looking for ")
    find_item(item)

elif str=="print":
    print_list()

elif str=="sort":
    sort_list()

elif str=="clear":
    clear_list()