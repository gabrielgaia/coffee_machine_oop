from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
order = Menu()
money = MoneyMachine()

should_continue = True

while should_continue:
    client_order = input(f"What would you like? ({order.get_items()}): ")
    if client_order == 'off':
        print("Bye!")
        should_continue = False
        exit(1)

    elif client_order == 'report':
        coffee_machine.report()
        money.report()
    else:
        client_order = order.find_drink(client_order)
        if client_order:
            if coffee_machine.is_resource_sufficient(client_order):
                if money.make_payment(client_order.cost):
                    coffee_machine.make_coffee(client_order)
