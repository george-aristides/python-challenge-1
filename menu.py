"""
I am making these  docstring block comments as notes for myself to better 
understand what is going on in my script.

I am probably not properly using them according to convention in Python.

Please let me know in the feedback if you find this kind of stuff helpful for 
grading/understanding what I am doing, or if I should omit these larger block 
notes in the future.

Thank you!
"""

while True:
    print("Dear Grader,")
    print("Please make sure to check the docstring at the top at some point in case you run this before looking at the code.")
    print("Press enter to continute.")
    print("Thank you!")
    complete = input("")
    match complete:
        case _:
            break

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie" : {
            "chocolate chip" : .99,
            "snickerdoodle" : .99
        },
        "Fresh Fruit" : {
            "apple" : .49,
            "banana" : .69
        },
        "Pita" : {
            "spanakopita" : 1.99,
            "tiropia" : 1.99
        } 
    },
    "Meals": {
        "Burrito": {
            "Beef": 7.99,
            "Chicken": 8.99,
            "Bean": 6.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Gyro": {
            "Chicken": 7.49,
            "Pork": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Greek": 2.49,
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Galaktoboureko": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).

    """
    For myself:

    This for loop takes the categories in the menu dictionary and assigns 
    each of them a number
        - The categories, i.e. snacks, meals, drinks, and dessert, are the keys
          in the dictionary
        - The information assigned to each key is the value, which in almost
          every case except dessert is another dictionary

    i is the number that is assigned to each category - each category gets
    a number key when printed, and after each iteration i is increased by 1

    So each menu key is assigned a key to identify it here
    """
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    """
    For myself:
    
    The challenge here is book-keeping considering the number of nested 
    dictionaries and other annoying stuff to keep track of

    Now we have assigned number keys to every category in the menu dictionary
    
    We have nested if else statements here
        - The first if else checks if the entry is a number
            - If it is it moves to the next if else
            - If it is not it prints "You didn't select a number."
            then moves to the match case statement 
        - The second if else if the number key you selected is one
        of the available options
            -If it is it saves the name of the category associated with the
                previously assigned number key to the new variable
                -It the prints the new variable, which has the name of the category
                -It then prompts to select the sub-elements of that menu catgory
                -We re-initialize the i=1 and menu_items dictionary here for the
                sub dictionaries stored within the values for each main category key
                -It prints some stuff for visual formatting ...
                -Now we have a for loop within the if statement
                    -The loop first checks if the value is another dictionary
                        -If it is a dictionary it creates enumerated key value 
                        pairs for the elements of the sub dictionary
                        -The rest is some visual formatting stuff to find how
                        how many spaces are needed to make things line up
                    -Else it just prints the items in the dictionary without 
                    needing to go through another sub dictionary
            -The Else for this case is if you select anything other than one 
            of the available number key options
        - The third if else is within the second if else, after the for loop
        that goes through all the items within the category or further 
        sub categories
            -It checks - since we just listed out some set of items within a
            category - if the user input selected is a number
                -It the checks if this number is one of the available options
                with another if else statement
                    -This if else again checks if the user input number is valid
                    as an option, stores it, and asks for a quantity
                        -Within this there is another if else that checks to see
                        if the quantity provided is a number, and if not 
                        it defaults to 1 
                    -Finally we interact with the order list we initialized a 
                    while back by appending the information - the item name,
                    price, and quantity - to the order list in the form of a 
                    dictionary with all of the information about each item
                    being a key value pair
            -Else it prints "You didn't select a number." and tells you you 
            didn't choose one of the options

    This all together should ensure that the user ends up selecting something 
    and there is no case where they continue without properly interacting with 
    the item selection process

    Since this process is not within but runs in sequence after a while loop,
    as long as the while loop condition is not broken the user can keep running 
    through this loop until they intentionally break the while loop
    """

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {item_name} would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_selection]["Price"],
                        "Quantity": quantity
                    })

                else:
                    # Tell the customer that their input isn't valid
                    print("You didn't select a number.")
            else:
                # Tell the customer they didn't select a menu option
                print(f"{menu_category} was not a menu option.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    """
    The final piece of the while loop is this match case statement

    This is the piece that can break the while loop we set at the beginning

    The match case means we can set multiple conditions to be met, and if one 
    of the conditions is met then the line indented below is executed

    in 
    """

    # Ask the customer if they would like to order anything else
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
        match keep_ordering:
            case "n":
                place_order = False
                break
            case "y":
                print("Thank you for your order.")
                break
            case _:
                print("Please type (Y)es to continue ordering or (N)o to complete your order.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${item['Price']} | {item['Quantity']}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total = sum([item["Price"] * item["Quantity"] for item in order])

# Print the total price of the order
print(f"\nTotal price: ${total:.2f}")
