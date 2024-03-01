# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
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
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

menu_dashes = "-" * 42
item_dashes = "-" * 46

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order = [ 
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
# Clear Order Dictionary
order.clear()
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

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
            print(menu_dashes)      
            # 2. Ask customer to input menu item number
            item = input(f"What {menu_category_name} item would you like to order?")
            # 3. Check if the customer typed a number
            if item.isdigit():
                if item == 'q':
                    break
            # Convert the menu selection to an integer
                item_number = int(item)
            # Check if the customer's input is a valid option
            # 4. Check if the menu selection is in the menu items
            if item_number in menu_items.keys():
            # Store the item name as a variable
                item_name = menu_items[item_number]["Item name"]
                item_price = menu_items[item_number]["Price"]
            # Ask the customer for the quantity of the menu item
                item_quantity = input(f"How many {item_name}\'s would you like to order?")
            # Check if the quantity is a number, default to 1 if not
                if item_quantity.isdigit():
                    order_price = float(item_price) * int(item_quantity)
                else:
                    item_quantity = 1
            # Append a new list to the order dictionary.  
                order_item_count = len(order)
                order_list = {"Item name": item_name, "Price": item_price, "Quantity": item_quantity}
                order.append(order_list)
            else:
            # Tell the customer that their input isn't valid
                print(f"{item} your input was not a menu item.")     
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
            print("You didn't select a number.")
    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").lower()
    # 5. Check the customer's input
    # Complete the order
    order_item_count = len(order)
    if(order_item_count > 0 and keep_ordering == 'n'):
        # Since the customer decided to stop ordering, thank them for
        # their order
            print("Thank You for your order.")
            # Print out the customer's order
            print("This is what we are preparing for you.\n")
            print("Item name                 | Price  | Quantity")
            print("--------------------------|--------|----------")
            # 6. Loop through the items in the customer's order and 
            # 7. Store the dictionary items as variables
            total_cost = []
            for element in order:
                for key in element:
                    if key == 'Item name':
                        list_item_name = element[key]
                    if key == 'Price':
                        list_price_print = '$' + str(element[key])
                        list_price = element[key]
                    if key == 'Quantity':
                        list_quantity_print = str(element[key])
                        list_quantity = element[key]
                    # 8. Calculate the number of spaces for formatted printing
                        num_item_spaces1 = 34 - len(list_item_name + list_price_print)
                        num_item_spaces2 = 12 - len(list_quantity_print)
                    # 9. Create space strings
                        item_spaces1 = " " * num_item_spaces1
                        item_spaces2 = " " * num_item_spaces2
                    # 10. Print the item name, price, and quantity
                        print(list_item_name + item_spaces1 + list_price_print + item_spaces2 + list_quantity_print)
                    # 11. Multiply the price by quantity for each item in the order and append it to total_cost list.
                        total_cost.append(float(list_price) * int(list_quantity))
            print(item_dashes) 
        # Calculate the total price of the order using list comprehension sum built in function
            print(f"Total Price for this Order:    ${format(sum(total_cost),'.2f')}")
            break
        
 

