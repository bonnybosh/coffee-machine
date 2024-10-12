
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": "$0"
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def program():

    end_of_task = False
    while not end_of_task:

        ask_user = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Function for checking sufficiency of remaining resource
        def check_resource():
            if ask_user == "espresso":
                if resources["water"] < MENU[ask_user]["ingredients"]["water"]:
                    print("Sorry there is not enough water")
                    program()
                elif resources["coffee"] < MENU[ask_user]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee")
                    program()
            else:
                if resources["water"] < MENU[ask_user]["ingredients"]["water"]:
                    print("Sorry there is not enough water")
                    program()
                elif resources["coffee"] < MENU[ask_user]["ingredients"]["coffee"]:
                    print("Sorry there is not enough coffee")
                    program()
                elif resources["milk"] < MENU[ask_user]["ingredients"]["milk"]:
                    print("Sorry there is not enough milk")
                    program()

        # function for printing report
        def generate_report():
            for key in resources:
                print(f"{key.title()} : {resources[key]}")

        # function that updates resources
        def update_resources_e():
            resources["money"] = f"${float(resources["money"][1:]) + MENU[ask_user]["cost"]}"
            if ask_user == "espresso":
                resources["water"] = resources["water"] - MENU[ask_user]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[ask_user]["ingredients"]["coffee"]
            else:
                resources["water"] = resources["water"] - MENU[ask_user]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[ask_user]["ingredients"]["coffee"]
                resources["milk"] = resources["milk"] - MENU[ask_user]["ingredients"]["milk"]

        #  Evaluate user choice of  coffee
        # print report
        if ask_user == "report":
            generate_report()
            program()

        # Turn off coffee machine
        if ask_user == "off":
            end_of_task = True

        if ask_user == "espresso" or ask_user == "latte" or ask_user == "cappuccino":
            check_resource()
            print("Please insert coins.")
            quarters_input = float(input("how many quarters?: "))
            dimes_input = float(input("how many dimes?: "))
            nickles_input = float(input("how many nickles?: "))
            pennies_input = float(input("how many pennies?: "))

            # Function to calculate total amount of coins inserted
            def t_coins_inserted():
                total = (quarters * quarters_input) + (dimes * dimes_input) + (nickles * nickles_input) + (
                        pennies * pennies_input)
                return total

            result = t_coins_inserted()

            # Function that checks whether coins inserted by user is enough
            def check_amount():
                if result >= MENU[ask_user]["cost"]:
                    balance = result - MENU[ask_user]["cost"]
                    # return balance
                    x = '{:0.2f}'.format(balance)
                    print(f"Here is ${x} in change\nHere is your {ask_user} Enjoy.")
                else:
                    print(f"insufficient funds, here is your ${'{:0.2f}'.format(result)}")
            update_resources_e()
            t_coins_inserted()
            check_amount()
            #program()


program()













