menu =  {

    "pasta": 60 , 
    "pizza" : 80 ,
    "coffee" : 100 ,
    "burger"  : 90 ,
    "lemon water"  : 120 ,
    }



print("WELCOME TO TRINITY RESTAURANT")
print("pasta : Rs60 \n, pizza : Rs80 \n coffee : Rs100 \n burger  : Rs90 \n lemon water : Rs120"  )


order_total = 0


item_1 = input("Enter the name of the item you want to order :: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f" {item_1} has been added to your order")

else:
    print("Item not available in the menu")

another_order  = input("Do you want to order anything else :: (Yes/No) ")
if another_order == "Yes" :
    item_2 = input("Please enter the item name :: ")
    if item_2 in menu:
        order_total += menu[item_2] 
        print(f"{item_2} added to your order")
    
    else:
        print("Item not available")

print(f"The total amount of your order is {order_total}")
