from data import MENU, resources

profit = 0


print("Greetings, how about a mug of coffee!")


def resource_check(order_list):
    for item in order_list:
        if order_list[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coins():
    print("Input coins.")
    total = int(input(" Insert number of quarters: "))*0.25
    total += int(input(" Insert number of dimes: ")) * 0.1
    total += int(input(" Insert number of nickles: ")) * 0.05
    total += int(input(" Insert number of  pennies: ")) * 0.01
    return total


def transaction_status(money_put, drink_cost):
    if money_put >= drink_cost:
        spare = round(money_put - drink_cost, 2)
        print(f"\nYour change: {spare}.")
        global profit
        profit += drink_cost

        return True
    else:
        print("Not enough.")
        return False


def coffee(drink_selected, ingredients_order):
    for item in ingredients_order:
        resources[item] -= ingredients_order[item]
    print(f"Phhhhssssss! Here is your {drink_selected}!")


machine_is_on = True

while machine_is_on:
    user_selection = input("Menu: 'Espresso', 'Latte', 'Cappuccino'. Type here: ").lower()
    if user_selection == 'off':
        machine_is_on = False
    elif user_selection == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_selection]
        if resource_check(drink["ingredients"]):
            payment = coins()
            if transaction_status(payment, drink["cost"]):
                coffee(user_selection, drink["ingredients"])
