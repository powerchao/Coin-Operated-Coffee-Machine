import assets
import os

def coffee_machine():
    water_capacity = assets.machine["water"]
    milk_capacity = assets.machine["milk"]
    coffee_capacity = assets.machine["coffee"]
    current_resources = {
        "water": assets.machine["water"],
        "milk": assets.machine["milk"],
        "coffee": assets.machine["coffee"],
    }
    total_sales = 0.0

    def refill(key, amount):
        if current_resources[key] + int(amount) > assets.machine[key]:
            print("You've made a mess and overfilled it. Better clean up.")
            return assets.machine[key]
        else:
            return current_resources[key] + int(amount)

    def report():
        current_coffee = current_resources["coffee"]
        current_water = current_resources["water"]
        current_milk = current_resources["milk"]
        print(f"The coffee machine has {current_coffee}g of coffee and can hold {coffee_capacity}g.")
        print(f"The coffee machine has {current_water}ml of water and can hold {water_capacity}ml.")
        print(f"The coffee machine has {current_milk}ml of milk and can hold {milk_capacity}ml.")
        friendly_sales = str(total_sales)
        while len(friendly_sales.split(".")[1])<2:
            friendly_sales += "0"
        print(f"The coffee machine has made ${friendly_sales} in sales so far.")
    
    def make_change(key,payed):
        return (payed-assets.recipes[key]["cost"])
    
    def can_order(key):
        if current_resources["coffee"] >= assets.recipes[key]["coffee"] and current_resources["milk"] >= assets.recipes[key]["milk"] and current_resources["water"] >= assets.recipes[key]["water"]:
            return True
        else:
            return False

    continuing = True
    while continuing:
        os.system("cls")
        print("Welcome to the coffee machine!\n")
        print("Your menu:\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00")
        print("You may also request a report of the machine's contents, or refill any ingredient in the machine.")
        user_action = input("What would you like to do? Type 'order', 'report', or 'refill'\n").lower()
        if user_action == "order":
            user_action = input("Which drink would you like to order? Type 'espresso', 'latte', or 'cappuccino'\n").lower()
            try:
                if can_order(user_action):
                    cost = str(assets.recipes[user_action]["friendly_cost"])
                    print(f"Your total is ${cost}")
                    payment_amount = 0.0
                    try:
                        payment_amount += (assets.coins["quarter"] * int(input("How many quarters are you paying with? ")))
                        payment_amount += (assets.coins["dime"] * int(input("How many dimes are you paying with? ")))
                        payment_amount += (assets.coins["nickel"] * int(input("How many nickels are you paying with? ")))
                        payment_amount += (assets.coins["penny"] * int(input("How many pennies are you paying with? ")))
                        change_due = round(make_change(user_action,payment_amount),2)
                        if change_due >= 0:
                            friendly_change = str(change_due)
                            while len(friendly_change.split(".")[1]) < 2:
                                friendly_change += "0"
                            print(f"Your change is ${friendly_change}.\nHere is your {user_action} \nEnjoy!")
                            total_sales += assets.recipes[user_action]["cost"]
                            current_resources["water"] -= assets.recipes[user_action]["water"]
                            current_resources["coffee"] -= assets.recipes[user_action]["coffee"]
                            current_resources["milk"] -= assets.recipes[user_action]["milk"]
                        else:
                            print(f"You did not pay enough to complete the transaction.\nYour ${payment_amount} has been refunded.")
                    except:
                        print("I'm not sure what kind of money you're trying to pay with, but we don't recognize it.")
                else:
                    print("Resources are too low to make that kind of drink.\nPlease run a report and refill what's necessary.")
            except:
                print("We do not offer that at this machine. Sorry.")
        elif user_action == "refill":
            user_action = input("Refill what? Type 'water', 'milk', or 'coffee'\n")
            user_amount = input("Refill by how much? \n")
            try:
                current_resources[user_action] = refill(user_action,user_amount)
                print("Refill successful.")
            except:
                print("The machine does not have a need for that.")
        elif user_action == "report":
            report()
        else:
            print("I'm sorry, I didn't catch that.")
        go_again = input("\nWould you like to continue using the machine? Type 'y' or 'n'\n")
        if go_again != 'y':
            continuing = False

coffee_machine()