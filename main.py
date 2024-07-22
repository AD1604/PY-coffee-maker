MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
from art import logo,cup
print(logo)

def is_resource_sufficient(order_ingredients):
    '''RETURNS TRUE IF ORDER IS MADE
    AND FALSE IF INGREDIENTS ARE INSUFFICIENT'''

    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"SORRY there is no enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    '''RETURNS TOTAL CALCULATED COINS INSERTED'''

    print("Please insert coins 💰 >>")
    total = int(input("How many Quarters 🪙 ? >> ")) * 0.25
    total += int(input("How many Dimes 🟡 ? >> ")) * 0.1
    total += int(input("How many Nickles 🪙 ? >> ")) * 0.05
    total += int(input("How many Pennies 🟤 ? >> ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''RETURNS TRUE IF PAYMENT IS ACCEPTED,
    FALSE --> IF MONEY IS INSUFFICIENT'''

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 3)
        print(f"CHANGE IS :{change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money . MONEY REFUNDED")
        return False


def make_coffee(drink_name, order_ingredients):
    '''deduct the required ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕☕ . ENJOY!!")
    print(cup)


is_on = True

while is_on:
    choice = input("What would You Like drink ? [EXPRESSO,LATTE,CAPPUCCINO]:").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g ")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
