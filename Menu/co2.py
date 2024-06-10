print("Welcome to \"CO2\"\n")
print("Here is our Menu:\n")

Signature_drinks = [
    "1. Lemon Mint",
    "2. Zeera Spicy",
    "3. Tangy Tamarind",
    "4. Pomegranate",
    "5. Ginger Mint",
    "6. Green Apple",
    "7. Blue Apple",
    "8. Atomic Plum",
    "9. Fresh Ginger",
    "10. Zeera Mint",
    "11. Lemon Spicy",
    "12. Zeera Masala",
    "13. Chilli Milli",
    "14. CO2 Power",
    "15. Red Grapes",
    "16. Mango Juice",
    "17. Peach Juice"
]

Cocktail_drinks = [
    "1. Rainbow Cocktail",
    "2. Wild Berry",
    "3. Berry Cocktail",
    "4. Apple Cocktail",
    "5. Fusion Blast",
    "6. Black Magic",
    "7. Blue Lagoon",
    "8. Bubble Up",
    "9. Vimto",
    "10. Lemon Cocktail",
    "11. Sting",
    "12. Berry Blossom"
]

Regular_drinks = [
    "1. Red Apple",
    "2. Raspberry",
    "3. Peach",
    "4. Blue Berry",
    "5. Frisky Orange",
    "6. Ice Cream Soda",
    "7. Strawberry",
    "8. Crazy Pineapple",
    "9. Black Berry",
    "10. Guava Thrill",
    "11. Lemon Lime",
    "12. Strawberry Lemonade",
    "13. Lychee Rose"
]

Doodh_Sodas = [
    "1. Pakola Milk Drink",
    "2. Chocolate Milk Drink",
    "3. Mango Milk Drink"
]

Milk_Shakes = [
    "1. Blue Berry Shake",
    "2. Mango Milk Shake",
    "3. Chocolate Milk Shake",
    "4. Strawberry Shake",
    "5. Vanilla Shake",
    "6. Oreo Shake",
    "7. Cold Coffee",
    "8. Kulfa Shake",
    "9. Pista Shake",
    "10. Bounty Shake",
    "11. Special Cold Coffee"
]

Hot_Beverage = [
    "1. Cappuccino",
    "2. Double Espresso",
    "3. Latte",
    "4. Kashmiri Tea",
    "5. Hot Chocolate Tea",
    "6. Cardamom Tea",
    "7. Karak Tea",
    "8. Mochaccino",
    "9. Chocolate Tea",
    "10. Espresso"
]

Icecreams = [
    "1. Mango",
    "2. Strawberry",
    "3. Pistachio",
    "4. Blue Berry",
    "5. Chocolate Plain",
    "6. French Vanilla",
    "7. Strawberry Cheesecake",
    "8. Blue Berry Cheesecake",
    "9. Pineapple",
    "10. Tutti Fruity",
    "11. Special Kulfa",
    "12. Bounty",
    "13. Chocolate Chip",
    "14. Butter Scotch",
    "15. Red Velvet",
    "16. Berry Blast"
]

R_Signature_drinks_price = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 150, 120, 120, 120]
L_Signature_drinks_price = [140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 140, 180, 140, 140, 140]

R_Cocktail_drinks_price = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
L_Cocktail_drinks_price = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120]

R_Regular_drinks_price = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
L_Regular_drinks_price = [120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120, 120]

R_Doodh_Sodas_price = [130, 220, 130]
L_Doodh_Sodas_price = [160, 300, 160]

S_Milk_Shakes_price = [330, 330, 330, 330, 350, 330, 350, 330, 330, 350, 400]

S_Hot_Beverage_price = [250, 250, 250, 170, 250, 170, 130, 150, 150, 170]

Single_Icecreams_price = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 120, 120, 120, 120, 120, 120]
Double_Icecreams_price = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 220, 220, 220, 220, 220, 220]
Family_Icecreams_price = [450, 450, 450, 450, 450, 450, 450, 450, 450, 450, 500, 500, 500, 500, 500, 500]

def signature_list():
    print("\nSIGNATURE DRINKS\n")
    for signature in Signature_drinks:
        print(signature)
    print("\n=============================")

def cocktail_list():
    print("\nCOCKTAIL DRINKS\n")
    for cocktail in Cocktail_drinks:
        print(cocktail)
    print("\n=============================")

def regular_list():
    print("\nREGULAR DRINKS\n")
    for regular in Regular_drinks:
        print(regular)
    print("\n=============================")

def doodh_list():
    print("\nDOODH SODAS\n")
    for doodh in Doodh_Sodas:
        print(doodh)
    print("\n=============================")

def shake_list():
    print("\nMILK SHAKES\n")
    for shake in Milk_Shakes:
        print(shake)
    print("\n=============================")

def beverage_list():
    print("\nHOT BEVERAGE\n")
    for bev in Hot_Beverage:
        print(bev)
    print("\n=============================")

def icecream_list():
    print("\nICE CREAMS\n")
    for ice in Icecreams:
        print(ice)
    print("\n=============================\n")

signature_list()
cocktail_list()
regular_list()
doodh_list()
shake_list()
beverage_list()
icecream_list()

Menu = [
"\n1. ┆ SIGNATURE DRINKS ┆",
   "2. ┆ COCKTAIL DRINKS  ┆",
   "3. ┆ REGULAR DRINKS   ┆",
   "4. ┆ DOODH SODAS      ┆",
   "5. ┆ MILK SHAKES      ┆", 
   "6. ┆ HOT BEVERAGE     ┆",
   "7. ┆ ICE CREAMS       ┆"
]

for m in Menu:
    print(m)
    
total_amount = 0

def place_order():
    global total_amount
    
    print("\nWrite the number for the category of drink you want to order (1 - 7)")
    Customer = int(input("Number  : "))
    
    if Customer == 1:
        print("\n=============================\n") 
        signature_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Signature_drinks[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        print("(Large 140 / regular 120 )")
        size1 = input("Enter a size : ").capitalize()
        quantity = int(input("\nEnter a quantity : "))
        if size1 == "Large":
            Selected_prize1 = L_Signature_drinks_price[Customer1 - 1] * quantity
        elif size1 == "Regular":
            Selected_prize1 = R_Signature_drinks_price[Customer1 - 1] * quantity
        else:
            print("Enter correct size")
            return
        
    elif Customer == 2:
        print("\n=============================\n") 
        cocktail_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Cocktail_drinks[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        print("(Large 120 / regular 100 )")
        size1 = input("Enter a size : ").capitalize()
        quantity = int(input("\nEnter a quantity : "))
        if size1 == "Large":
            Selected_prize1 = L_Cocktail_drinks_price[Customer1 - 1] * quantity
        elif size1 == "Regular":
            Selected_prize1 = R_Cocktail_drinks_price[Customer1 - 1] * quantity
        else:
            print("Enter correct size")
            return
        
    elif Customer == 3:
        print("\n=============================\n") 
        regular_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Regular_drinks[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        print("(Large 140 / regular 120 )")
        size1 = input("Enter a size : ").capitalize()
        quantity = int(input("\nEnter a quantity : "))
        if size1 == "Large":
            Selected_prize1 = L_Regular_drinks_price[Customer1 - 1] * quantity
        elif size1 == "Regular":
            Selected_prize1 = R_Regular_drinks_price[Customer1 - 1] * quantity
        else:
            print("Enter correct size")
            return

    elif Customer == 4:
        print("\n=============================\n") 
        doodh_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Doodh_Sodas[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        print("(Large 160 / regular 130 )")
        size1 = input("Enter a size : ").capitalize()
        quantity = int(input("\nEnter a quantity : "))
        if size1 == "Large":
            Selected_prize1 = L_Doodh_Sodas_price[Customer1 - 1] * quantity
        elif size1 == "Regular":
            Selected_prize1 = R_Doodh_Sodas_price[Customer1 - 1] * quantity
        else:
            print("Enter correct size")
            return

    elif Customer == 5:
        print("\n=============================\n") 
        shake_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Milk_Shakes[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        quantity = int(input("\nEnter a quantity : "))
        Selected_prize1 = S_Milk_Shakes_price[Customer1 - 1] * quantity

    elif Customer == 6:
        print("\n=============================\n") 
        beverage_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Hot_Beverage[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        quantity = int(input("\nEnter a quantity : "))
        Selected_prize1 = S_Hot_Beverage_price[Customer1 - 1] * quantity

    elif Customer == 7:
        print("\n=============================\n") 
        icecream_list()
        print("\nEnter a number to place an order")
        Customer1 = int(input("Number : "))
        Selected_item1 = Icecreams[Customer1 - 1]
        print(f"\nSelected Item : {Selected_item1}\n")
        print("(single  / double / family)")
        size1 = input("Enter a size : ").capitalize()
        quantity = int(input("\nEnter a quantity : "))
        if size1 == "Single":
            Selected_prize1 = Single_Icecreams_price[Customer1 - 1] * quantity
        elif size1 == "Double":
            Selected_prize1 = Double_Icecreams_price[Customer1 - 1] * quantity
        elif size1 == "Family":
            Selected_prize1 = Family_Icecreams_price[Customer1 - 1] * quantity
        else:
            print("Enter correct size")
            return

    else:
        print("Enter a correct number")
        return

    total_amount += Selected_prize1
    print(f"\nTotal amount for this order: {Selected_prize1}")
    print(f"Running total: {total_amount}")

while True:
    place_order()
    more_orders = input("\nDo you want to place another order? (yes/no): ").strip().lower()
    if more_orders != 'yes':
        break

print(f"\nFinal total amount: {total_amount}\nThank you for your order!")
