#STEP II
grocery_prices = {"Chicken": 1.59, "Beef":1.99, "Cheese":1.0, "Milk": 2.5}

#STEP III
birth_years = {"Tais": 2010, "Liz": 2000, "Uli": 1990}

#STEP IV
chicken = grocery_prices["Chicken"]
beef = grocery_prices["Beef"]
cheese = grocery_prices["Cheese"]
milk = grocery_prices["Milk"]
print(chicken, beef, cheese, milk)

#STEP V
tais = birth_years["Tais"]
liz = birth_years["Liz"]
uli = birth_years["Uli"]
print(tais, liz, uli)

birth_years["Tais"] -= 1

#STEP VI
shoe_inventory = {
    "Jordan 13": 1, "Yeezy": 8,"Foamposite": 10, "Air Max": 5, "SB Dunk": 20}
shoe_inventory["SB Dunk"] -= 2
shoe_inventory["Yeezy"] += 1

shoe_inventory["Jordan 13"] += 7
shoe_inventory["Yeezy"] += 7
shoe_inventory["Foamposite"] += 7
shoe_inventory["Air Max"] += 7
shoe_inventory["SB Dunk"] += 7

shoe_inventory["Jordan 13"] -= 3
shoe_inventory["Yeezy"] -= 3
shoe_inventory["Foamposite"] -= 3
shoe_inventory["Air Max"] -= 3
shoe_inventory["SB Dunk"] -= 3