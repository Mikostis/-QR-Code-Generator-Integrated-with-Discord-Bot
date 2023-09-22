import time


# Initialize resources
water = 300  # in ml
milk = 200   # in ml
coffee = 100  # in g
money = 0    # in dollars

# Define the menu with drink options and their ingredients
menu = {
    'espresso': {'water': 50, 'coffee': 18, 'cost': 1.5},
    'latte': {'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.5},
    'cappuccino': {'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.0}
}

while True:
    # Step 1: Prompt user for their choice
    try:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino/off/report): ").lower()

        # Turn off the Coffee Machine
        if user_choice == 'off':
            break

        # Print report
        if user_choice == 'report':
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
            continue

        # Check resources sufficient
        if user_choice not in menu:
            print("Invalid choice. Please choose a valid option.")
            continue

        selected_drink = menu[user_choice]
        drink_cost = selected_drink['cost']

        insufficient_ingredient = None
        for ingredient, quantity in selected_drink.items():
            if ingredient != 'cost' and selected_drink[ingredient] > locals()[ingredient]:
                insufficient_ingredient = ingredient
                break

        if insufficient_ingredient:
            print(
                f"Sorry, there is not enough {insufficient_ingredient}. Refilling...")
            time.sleep(3)  # Simulate a 3-second refill delay
            water = 300  # Reset water quantity
            milk = 200   # Reset milk quantity
            coffee = 100  # Reset coffee quantity
            print("Refill complete. You can enjoy your coffee now.")
            continue

        # Step 5: Process coins
        print("Please insert coins.")
        try:
            quarters = int(input("Quarters: ")) * 0.25
            dimes = int(input("Dimes: ")) * 0.10
            nickels = int(input("Nickels: ")) * 0.05
            pennies = int(input("Pennies: ")) * 0.01
        except ValueError:
            print("Invalid input for coins. Please enter valid numbers.")
            continue

        total_inserted = quarters + dimes + nickels + pennies

        # Step 6: Check transaction successful
        if total_inserted < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue
        elif total_inserted > drink_cost:
            change = total_inserted - drink_cost
            print(f"Here is ${change:.2f} in change.")

        money += drink_cost

        # Step 7: Make Coffee
        print(f"Making your {user_choice}...")

        # Deduct ingredients
        for ingredient, quantity in selected_drink.items():
            if ingredient != 'cost':
                locals()[ingredient] -= quantity

        print(f"Here is your {user_choice}. Enjoy!")

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break

# End of the program
