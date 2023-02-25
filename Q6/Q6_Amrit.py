# money should not be floats, but I dont care!
FAST_FOOD_DICTIONARY = {
    "Big Mac": 5.99,
    "Papa Burger": 8.99,
    "French Fries": 3.29,
    "Soft Serve Ice Cream": 1.29,
    "Baconator": 12.99,
    "Filet-O-Fish": 5.99,
    "Chicken Tenders": 8.49,
    "Smash Burger": 6.49,
    "Peanuts": 0.50,
    "Quarter Pounder": 7.29,
    "Iced Coffee": 2.49,
    "Jalepeno Poppers": 5.99,
    "Buttered Corn": 1.49,
    "Popcorn Chicken": 5.49,
    "Fried Chicken": 10.99
}

money = float(input('How much money do you have? '))
while True:
    print("You have ${:.2f}".format(money))
    print("What would you like to buy?")
    for food in FAST_FOOD_DICTIONARY:
        print(f"{food} - ${FAST_FOOD_DICTIONARY[food]}")
    food = input("Enter the name of the food you want to buy: ")
    food = food.title()

    if food not in FAST_FOOD_DICTIONARY:
        print("Sorry, we don't have that food.")
        print("You have been fined $1 for wasting our time.")
        money -= 1
        continue

    if money < FAST_FOOD_DICTIONARY[food]:
        print("Sorry, you don't have enough money for that.")
        print("Get out of my store!")
        break

    money -= FAST_FOOD_DICTIONARY[food]
    print("Thank you for your purchase!")
    print("Have fun contributing to the global obesity epidemic!")
