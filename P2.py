# Guacamole Search

""" The linear search is used to find an item in a list. 
The items do not have to be in order. 
To search for an item, start at the beginning of the list and continue searching until either the end of the list is reached or the item is found.
"""


ingredients = ["1 tbsp cilantro", "2 avocados", "1 lime" , "1 tsp salt", "1/2 onion"]


# TODO: Implement the function which adds an ingredient to the list
def add_ingredient(ingredient):
    global ingredients
    ingredients.append('2 meal')
    return ingredients
print(add_ingredient(" "))

# TODO: Implement the function which removes and returns the last ingredient in the list
def pop_ingredient():
    global ingredients
    ingredients.pop()
    return ingredients
print(pop_ingredient())

# TODO: Implement the function which removes and returns an ingredient at the given index
def pop_ingredient_at(index):
    global ingredients
    ingredients.pop(2)
    return ingredients
print(pop_ingredient_at(5))

# TODO: Implement the function which counts and returns the number of needed ingredients
def count_ingredients():
    global ingredients
    i=0
    for i in range(i,len(ingredients)+1):
        i +=1
    return i
print(count_ingredients())

# TODO: Implement the function which print the number of ingredients needed and a tabbed list of ingredients
def pretty_recipe():
    i=0
    for i in range(i,len(ingredients)):
        i +=1
    return i
print(pretty_recipe())

# TODO: 
# * Implement the linear search algorithm on the list of ingredients.
# * Test that it works with ingredients in and not in the list.
# * Add a counter to keep track of how many searches have been done for each item searched for.
# * Add the functionality to add an item to the list if it is not found.

def search_for_ingredient(ingredient,x):
    for i in range(len(ingredients)):
      if ingredients[i] == x:
        return i
   


# TODO: Call your functions here to test your code.
search_for_ingredient('2 meal' , 4)