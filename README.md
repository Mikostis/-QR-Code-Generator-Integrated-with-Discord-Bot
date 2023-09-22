
# Coffee Machine Program Documentation

This program simulates a coffee machine that takes user orders, checks resources, processes payments, and makes coffee.

How It Works:
1. The program starts and prompts the user for their coffee order.
2. It checks if there are enough resources (water, milk, coffee) to make the selected coffee.
3. If there are insufficient resources, the program initiates a refill process (waiting 3 seconds) and then continues.
4. The user is prompted to insert coins (quarters, dimes, nickels, pennies) to pay for the coffee.
5. The program checks if the payment is sufficient.
6. If the payment is sufficient, it deducts the resources, processes the payment, and makes the coffee.
7. The program provides change if necessary and serves the coffee.

Techniques Used:
- User input is obtained using the input() function.
- The program uses if-elif-else statements to handle different user inputs.
- Resources are tracked using variables (e.g., water, milk, coffee, money).
- Error handling is implemented to handle cases of insufficient resources or payment.
- The program uses functions to modularize the code.
- A while loop ensures that the program keeps running for multiple orders.

Resource Refill:
- When there are insufficient resources, the program initiates a refill process.
- During the refill, the program waits for 3 seconds to simulate the refill process.
- After the refill, the program can serve the next customer.

Usage:
1. Run the program.
2. Enter the coffee order (espresso, latte, cappuccino) when prompted.
3. Follow the on-screen instructions to insert coins.
4. Enjoy your coffee!