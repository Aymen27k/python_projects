MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money} $")


def check_resources(resources, coffee_req):
    for item in coffee_req:
        if resources[item] < coffee_req[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def coffee_requirements(menu, coffee):
    req_res = {}
    for item in menu:
        water = menu[coffee]['ingredients']['water']
        milk = menu[coffee]['ingredients']['milk']
        coffee_amount = menu[coffee]['ingredients']['coffee']
        coffee_price = menu[coffee]['cost']
    req_res['water'] = water
    req_res['milk'] = milk
    req_res['coffee'] = coffee_amount
    return req_res, coffee_price


def calculate_coins(quarters, dimes, nickles, pennies):
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    total_inputted_coins = quarters_total + dimes_total + nickles_total + pennies_total
    return total_inputted_coins


def check_payment_sufficient(total_coins, coffee_price):
    if total_coins < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True


def change_calculator(total_coins, coffee_price):
    change = total_coins - coffee_price
    return change


def update_resources(resources, consumed_materials, coffee_price):
    resources['water'] -= consumed_materials['water']
    resources['milk'] -= consumed_materials['milk']
    resources['coffee'] -= consumed_materials['coffee']
    resources['money'] += coffee_price


continue_execution = False


def main():
    user_input = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if user_input == "report":
        report(resources)
    elif user_input == 'exit':
        return True
    else:
        coffee_req, coffee_price = coffee_requirements(MENU, user_input)
        available_resources = check_resources(resources, coffee_req)
        if available_resources:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_coins = calculate_coins(quarters, dimes, nickles, pennies)
            payment_verification = check_payment_sufficient(total_coins, coffee_price)
            if payment_verification:
                customer_change = change_calculator(total_coins, coffee_price)
                print(f"Here is {customer_change} in change.")
                print(f"Here is your {user_input} ☕ Enjoy")
                update_resources(resources, coffee_req, coffee_price)


while not continue_execution:
    if __name__ == "__main__":
        continue_execution = main()
