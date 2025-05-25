from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
menu = Menu()
payment = MoneyMachine()


continue_execution = False


def main():
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}: ").lower()
    if user_choice == 'report':
        coffe_machine.report()
        payment.report()
    elif user_choice == "exit":
        return True
    else:
        chosen_drink = menu.find_drink(user_choice)
        is_doable = coffe_machine.is_resource_sufficient(chosen_drink)
        if is_doable:
            payment_verification = payment.make_payment(chosen_drink.cost)
            if payment_verification:
                coffe_machine.make_coffee(chosen_drink)


while not continue_execution:
    if __name__ == "__main__":
        continue_execution = main()
