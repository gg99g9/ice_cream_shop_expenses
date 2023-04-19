# Filename: main.py

"""
This program does the following:
  1. Allows income and expenses to be updated.
  2. Calculates monthly profit/loss
  3. Performs "what-if" analysis

I verified the inputs using the test cases below.
"""


#  Default values
serving_cost = 1.00
labor_rate = 7.50
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 1000
selling_price = 4.00


"""
# Test Case 1: Realistic
serving_cost = 3.0
labor_rate = 15.0
shop_rental = 2000
utilities = 500
advertising = 250
servings_per_month = 1000
selling_price = 9.0
"""

"""
# Test Case 2: Optimistic
serving_cost = 2.5
labor_rate = 14.5
shop_rental = 1500
utilities = 500
advertising = 0
servings_per_month = 1500
selling_price = 8.5
"""

"""
# Test Case 3: Pessimistic
serving_cost = 4.5
labor_rate = 16.0
shop_rental = 2200
utilities = 750
advertising = 500
servings_per_month = 800
selling_price = 8.5
"""

""" 
# Test Case 4: Error
serving_cost = 1
labor_rate = 7.5
shop_rental = 800
utilities = 150
advertising = 100
servings_per_month = 0
selling_price = 4
"""

# Run program loop
run_program = True
while run_program:

    # Run calculations
    MONTHLY_LABOR_COST = labor_rate * 8 * 6 * 4
    EXPENSES_PER_MONTH = shop_rental + utilities + advertising + MONTHLY_LABOR_COST + (serving_cost * servings_per_month)
    INCOME_PER_MONTH = selling_price * servings_per_month
    PROFIT_LOSS_PER_MONTH = INCOME_PER_MONTH - EXPENSES_PER_MONTH
    # Zero division error handling
    if servings_per_month == 0:
        PROFIT_LOSS_PER_SERVING = 0
    else:
        PROFIT_LOSS_PER_SERVING = PROFIT_LOSS_PER_MONTH / servings_per_month

    # Menu
    print("")
    print("MENU")
    print("Expenses:")
    print("1. Cost per serving:", round(serving_cost, 2))
    print("2. Labor rate per hour:", round(labor_rate, 2))
    print("3. Shop rental per month:", round(shop_rental, 2))
    print("4. Utilities per month:", round(utilities, 2))
    print("5. Advertising budget per month:", round(advertising, 2))
    print("Income:")
    print("6. Selling price (each):", round(selling_price, 2))
    print("7. Servings sold per month:", servings_per_month)
    print("Analysis: ")
    print("8. Profit/Loss Calculation")
    print("9. \"What If\" analysis with 10% variance")
    print("")

    # Select from menu
    selection = input("Enter a menu item (0 to exit): ")

    # Invalid entry loop - selection not a digit
    while selection.isdigit() == False:
        selection = input("Entry not valid. Enter a menu item between 1 and 9, or enter 0 to exit: ")

    # Cast selection string to float
    selection = float(selection)

    # Invalid entry loop - selection not an integer between 0 and 9
    while selection % 1 != 0 or selection < 0 or selection > 9:
        selection = float(input("Entry not valid. Enter a menu item between 1 and 9, or enter 0 to exit: "))

    # Item 1 selected - serving cost
    if selection == 1:
        serving_cost = round((float(input("Enter cost per serving: "))), 2)
        # Invalid entry loop
        while float(serving_cost) < 0:
            serving_cost = round((float(input("Entry cannot be less than 0.00. Enter cost per serving: "))), 2)

    # Item 2 selected - labor rate
    elif selection == 2:
        labor_rate = round((float(input("Enter labor rate per hour: "))), 2)
        # Invalid entry loop
        while labor_rate < 0:
            labor_rate = round((float(input("Entry cannot be less than 0.00. Enter labor rate per hour: "))), 2)

    # Item 3 selected - shop rent
    elif selection == 3:
        shop_rental = round((float(input("Enter shop rental per month: "))), 2)
        # Invalid entry loop
        while shop_rental < 0:
            shop_rental = round((float(input("Entry cannot be less than 0.00. Enter shop rental per month: "))), 2)

    # Item 4 selected - utilities
    elif selection == 4:
        utilities = round((float(input("Enter utilities per month: "))), 2)
        # Invalid entry loop
        while utilities < 0:
            utilities = round((float(input("Entry cannot be less than 0.00. Enter utilities per month: "))), 2)

    # Item 5 selected - advertising
    elif selection == 5:
        advertising = round((float(input("Enter advertising budget per month: "))), 2)
        # Invalid entry loop
        while advertising < 0:
            advertising = round((float(input("Entry cannot be less than 0.00. Enter advertising budget per month: "))), 2)

    # Item 6 selected - selling price
    elif selection == 6:
        selling_price = round((float(input("Enter selling prince (each): "))), 2)
        # Invalid entry loop
        while selling_price < 0:
            selling_price = round((float(input("Entry cannot be less than 0.00. Enter selling prince (each): "))), 2)

    # Item 7 selected - servings per month
    elif selection == 7:
        servings_per_month = input("Enter servings sold per month: ")

        # Invalid entry loop - servings per month not a digit
        while servings_per_month.isdigit() == False:
            servings_per_month = input(
                "Entry cannot be a decimal or less than 0. Enter servings per month: ")

        # Cast servings per month string to float
        servings_per_month = float(servings_per_month)

        # Invalid entry loop - servings per month not an integer
        while servings_per_month % 1 != 0 or servings_per_month < 0:
            servings_per_month = input(
                "Entry cannot be a decimal or less than 0. Enter servings per month: ")

        # Cast servings per month float to integer
        servings_per_month = int(servings_per_month)

        # Zero division error handling
        if servings_per_month == 0:
            PROFIT_LOSS_PER_SERVING = 0

    # Item 8 selected - Monthly profit/loss
    elif selection == 8:
        print("MONTHLY PROFIT/LOSS")
        print("The Ice Cream Shop will have a monthly profit/loss of", round(PROFIT_LOSS_PER_MONTH, 2), "or", round(PROFIT_LOSS_PER_SERVING, 2), "per serving.")

    # Item 9 selected - "What-if" analysis
    elif selection == 9:
        print("")
        print("\"WHAT-IF\" ANALYSIS WItH 10% VARIANCE")
        print("Varying the Expenses From -10% to +10%:")
        # Expenses
        for i in range(-10, 11, 2):
            VARYING_EXPENSES = EXPENSES_PER_MONTH * (100 + i) / 100
            VARYING_EXPENSES_PROFIT_LOSS = (INCOME_PER_MONTH - VARYING_EXPENSES)
            print("Percent:", i, " Expenses:", round(VARYING_EXPENSES, 2), " Profit/Loss:",
                  round(VARYING_EXPENSES_PROFIT_LOSS, 2))
        print("")
        print("Varying the Income From -10% to +10%:")
        # Income
        for i in range(-10, 11, 2):
            VARYING_INCOME = INCOME_PER_MONTH * (100 + i) / 100
            VARYING_INCOME_PROFIT_LOSS = (VARYING_INCOME - EXPENSES_PER_MONTH)
            print("Percent:", i, " Income:", round(VARYING_INCOME, 2), " Profit/Loss:", round(VARYING_INCOME_PROFIT_LOSS, 2))

    # Exit the program
    elif selection == 0:
        print("You have exited the program.")
        break

    # Update calculations
    MONTHLY_LABOR_COST = labor_rate * 8 * 6 * 4
    EXPENSES_PER_MONTH = shop_rental + utilities + advertising + MONTHLY_LABOR_COST + (serving_cost * servings_per_month)
    INCOME_PER_MONTH = selling_price * servings_per_month
    PROFIT_LOSS_PER_MONTH = INCOME_PER_MONTH - EXPENSES_PER_MONTH
    # Zero division error handling
    if int(servings_per_month) == 0:
        PROFIT_LOSS_PER_SERVING = 0
    else:
        PROFIT_LOSS_PER_SERVING = PROFIT_LOSS_PER_MONTH / servings_per_month

    """
    # Prints variables and constants for testing
    print("")
    print("VARIABLES AND CONSTANTS")
    print("serving_cost:", round(serving_cost, 2))
    print("labor_rate:", round(labor_rate, 2))
    print("shop_rental:", round(shop_rental, 2))
    print("utilities:", round(utilities, 2))
    print("advertising:", round(advertising, 2))
    print("selling_price:", round(selling_price, 2))
    print("servings_per_month:", round(servings_per_month, 2))
    print("MONTHLY_LABOR_COST:", round(MONTHLY_LABOR_COST, 2))
    print("EXPENSES_PER_MONTH:", round(EXPENSES_PER_MONTH, 2))
    print("INCOME_PER_MONTH:", round(INCOME_PER_MONTH, 2))
    print("PROFIT_LOSS_PER_MONTH:", round(PROFIT_LOSS_PER_MONTH, 2))
    # Zero division error handling
    if int(servings_per_month) == 0:
        print("PROFIT_LOSS_PER_SERVING: ", PROFIT_LOSS_PER_SERVING)
    else:
        print("PROFIT_LOSS_PER_SERVING:", round(PROFIT_LOSS_PER_SERVING, 2))
    """