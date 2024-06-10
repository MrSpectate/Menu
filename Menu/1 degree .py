print("\nWELCOME TO 1°C\n")
print("HERE IS OUR MENU\n")

# 1°C DRINKS MENU

Menu = [
    "1. Boylan's Soda : $120 ",
    "2. Blue Sky Soda : $130 ",
    "3. Jarritos : $140 ",
    "4. Cheerwine : $160 ",
    "5. Big Red : $120 ",
    "6. Murree Brewery : $150 ",
    "7. Shandy Cola : $130 ",
    "8. Mirinda : $140 ",
    "9. Next Peach : $130 ",
    "10. Crush : $150",
]

# Prices of 1°C
prices = [120, 130, 140, 160, 120, 150, 130, 140, 130, 150]

for m in range(len(Menu)):
    print(Menu[m])

# Customer order
Customer_choice = int(input("\nPlease select a number to place an order : "))

selected_item = Menu[Customer_choice - 1]
print(f"You selected a |{selected_item}|")

# Customer deciding quantity
quantity = int(input("Enter how many: "))

selected_price = prices[Customer_choice - 1] * quantity

# Total drink price
print(f"Your drink's bill is: ${selected_price}")

# Persuade for ice cream
print("We have a good deal running on ice cream here. Would you like to take advantage of it?")

# Yes or no input
user = input("\nY/N: ").upper()

if user == "Y":
    print("\nSure, here is the ice cream menu:\n")

    # Ice cream menu
    icecreams = [
        "1. Honey Lavender Dream : $399",
        "2. Spiced Chai Infusion : $499",
        "3. Blueberry Balsamic Blast : $299",
        "4. Avocado Lime Fiesta : $599",
        "5. Cardamom Crunch Delight : $600",
    ]

    # Ice cream prices
    prices_ice = [399, 499, 299, 599, 600]

    for i in range(len(icecreams)):
        print(icecreams[i])

    Customer_choice_ice = int(input("\nPlease select a number to place an order: ")) - 1

    selected_item_ice = icecreams[Customer_choice_ice]
    print(f"You selected a {selected_item_ice}")

    quantity_ice = int(input("Enter how many: "))

    selected_price_ice = prices_ice[Customer_choice_ice] * quantity_ice
    print(f"Your ice cream's bill is: ${selected_price_ice}")

    total_bill = selected_price_ice + selected_price
    print(f"Here is your total bill: ${total_bill}")
else:
    print("Okay, sure. Thank you for coming!")
