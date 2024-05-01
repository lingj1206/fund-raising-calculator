import pandas


def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    while True:
        response = input(question)

        if response == "":
            print(f"{error}.  \nP;ease try again.\n")
            continue

        return response


def currency(x):
    return f"${x:.2f}"


# main routine starts here

# set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# get user data
product_name = not_blank("product name: ",
                         "The product name can't be blank")

# loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":
    print()
    # get name, quantity and item
    item_name = not_blank("Item name: ",
                          "The component name can't be blank.")
    if item_name.lower() == "xxx":
        break

    quantity = num_check("Quantity: ",
                         "The amount must be a whole number"
                         "more than zero",
                         int)
    price = num_check("How much for a single item? $",
                      "The price must be a number (more than zero)",
                      float)

    #     add item, quantity and prices to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# calculate the cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# find subtotal
variable_sub = variable_frame['Cost'].sum()

# currency formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# PRINTING AREA
print(variable_frame)
print()
print(f"Variable costs: ${variable_sub:.2sf}")
