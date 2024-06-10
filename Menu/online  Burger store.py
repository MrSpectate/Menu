print("\nWELCOME TO \"Spectural Burger\"\n")
print("Here is Our Menu : \n")

Menu = [

      
          "1* Chicken Burger with cheese : $600",
          "2* MR.ZEE with cheese : $700",
          "3* Chicken BIG with cheese : $599",
          "4* Chicken Triple with cheese : $1000",
          "5* Egg n Chicken : $200",
          "6* Mr Big Deluxe : $799",
          "7* Mr Big With Egg : $700",
          "8* MR.BURGER with cheese : $999",
          "9* Nuggets 6 pcs : $370",
         "10* Nuggets 12 pcs : $720"
]

Prizes = [600,700,599,1000,200,799,700,999,370,720]

for m in range(len(Menu)):
    print(Menu[m])

user_choice = int(input("\nPlease select item to order : "))

selected_item = Menu[user_choice - 1]

print(f"Selected item is : |{selected_item}|")

quantity = int(input("Quantity : "))

total_prize = Prizes[user_choice - 1 ] * quantity

print("Here is you total prize : ",total_prize)

print("\nEnter the information\n")

name = input(" your name: ")
number = int(input(" your number: "))
Address = input("your Address: ")

print("\n***ORDER***\n")
print(f"\nItem : {selected_item}")
print(f"Quantity : {quantity}")
print(f"Total prize : {total_prize}\n")

print("\n***DETAILS***\n")
print(f"Name : {name}")
print(f"Number :  {number}")
print(f"Address : {Address}")



print("\n Your order has been received. Your order will be delivered to your home within 15 minutes.")
print("\nEnjoy your meal!!!")









