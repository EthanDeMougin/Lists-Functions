#  Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = ["mozzarella", "cinderella", "salmonella"]

# Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
things[1] = things[1].capitalize()
print(things)

# Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things)

# Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[2]
print(things)

# Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].


# Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.
