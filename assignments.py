import time
import math
import random

def main():
    print("\nWelcome to MIT's Intro to Python Course!\n")
    time.sleep(0.5)

    print("Here, you can find my responses to each pset.\n")
    time.sleep(0.5)

    while True:
        try:
            selection = int(input("Input the pset you'd like to see! "))
        except (ValueError):
            print("Please enter a number.")
            continue

        if (selection > 5) or (selection < 0):
            print("Invalid response :(\npsets start at 0 and end at 5.\nPlease input a number from 0-5.\n")
        else:
            if selection == 0:
                pset0()
                break
            if selection == 1:
                pset1()
                break

def pset0():
    print("Welcome to pset0!")
    input("Hit enter to see the solutions for exercises 1-5: ")

    s1 = 6+4*10
    print("1) 6+4*10 =", s1)

    s2 = (6+4)*10
    print("2) (6+4)*10 =", s2)

    s3 = 23.0**5
    print("3) 23.0^5 =", s3)

    # Equation: 34*x^2 + 68*x - 510
    s4 = (-68 + math.sqrt((68**2) - (4 * 34 * -510))) / (2 * 34)
    print("4) In the equation: (34*x^2 + 68*x - 510), x1 =", s4)

    s5 = math.cos(3.4)**2 + math.sin(3.4)**2
    print("5) cos(3.4)^2 + sin(3.4)^2 =", s5)

def pset1():
    print("Welcome to pset1!")
    print("Which Part would you like to see?")
    part = input("Enter A, B, or C: ")
    
    if part == "A":
        print("\nPart A: House Hunting\n")
        print("Calculate how many months it will take to save enough for a down payment.\n")
        time.sleep(0.5)

        # User inputs
        annual_salary = input("Enter your annual salary: ")
        if len(annual_salary) < 1:
            annual_salary = 120000
        portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
        if len(portion_saved) < 1:
            portion_saved = 0.10
        total_cost = input("Enter the cost of your dream home: ")
        if len(total_cost) < 1:
            total_cost = 1000000

        # Cast types
        annual_salary = int(annual_salary)
        portion_saved = float(portion_saved)
        total_cost = int(total_cost)

        # Set variables
        portion_down_payment = 0.25
        current_savings = 0
        r = 0.04
        month_count = 0

        down_payment_cost = total_cost * portion_down_payment
        monthly_salary = annual_salary / 12
        monthly_addition = monthly_salary * portion_saved

        # Loop until goal
        while current_savings < down_payment_cost:
            month_count += 1
            # First month won't gain any interest
            if month_count > 1:
                monthly_interest = current_savings * r / 12
                current_savings += monthly_interest
            current_savings += monthly_addition

        print("Number of months:", month_count)


    elif part == "B":
        print("\nPart B: Saving, with a raise\n")
        print("Calculate how many months it will take to save enough for a down payment.\n")
        time.sleep(0.5)

        # User inputs
        annual_salary = input("Enter your annual salary: ")
        if len(annual_salary) < 1:
            annual_salary = 120000
        portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
        if len(portion_saved) < 1:
            portion_saved = 0.05
        total_cost = input("Enter the cost of your dream home: ")
        if len(total_cost) < 1:
            total_cost = 500000
        semi_annual_raise = input("Enter the semi-annual raise, as a decimal: ")
        if len(semi_annual_raise) < 1:
            semi_annual_raise = 0.03

        # Cast types
        annual_salary = int(annual_salary)
        portion_saved = float(portion_saved)
        total_cost = int(total_cost)
        semi_annual_raise = float(semi_annual_raise)

        # Set variables
        portion_down_payment = 0.25
        current_savings = 0
        r = 0.04
        month_count = 0
        down_payment_cost = total_cost * portion_down_payment

        # Loop until goal
        while current_savings < down_payment_cost:
            # Increase salary every 6 months
            if month_count > 0 and (month_count % 6) == 0:
                annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
            monthly_addition = monthly_salary * portion_saved
            # First month won't gain any interest
            if month_count >= 1:
                monthly_interest = current_savings * r / 12
                current_savings += monthly_interest
            current_savings += monthly_addition
            month_count += 1

        print("Number of months:", month_count)

    elif part == "C":
        # Find the percentage of your salary to save
        # in order to get to $250K in 36 months.
        # You get a 7% raise twice a year and 
        # you get a 4% return on your savings.
        print("\nPart C: Finding the right amount to save away\n")
        print("Calculate how much you should save each month to achieve your goal.\n")
        time.sleep(0.5)  
    
        # User input
        annual_salary = input("Enter the starting salary: ")
        if len(annual_salary) < 1:
            annual_salary = 150000

        # Cast type
        annual_salary = int(annual_salary)

        # Set variables
        semi_annual_raise = 0.07
        r = 0.04
        portion_down_payment = 0.25
        total_cost = 1000000
        month_count = 0
        current_savings = 0
        down_payment_cost = total_cost * portion_down_payment
        steps = 0

        # Create rate options list
        rates = []
        i = 0
        while i < 10000:
            rates.append(i + 1)
            i += 1

        check(rates, month_count, annual_salary, semi_annual_raise, current_savings, r, down_payment_cost, steps)

    else:
        print("Must input either A, B, or C")

# Check if a test rate is the right number
def check(rates, month_count, annual_salary, semi_annual_raise, current_savings, r, down_payment_cost, steps):
    # Pick a test rate from the middle of our list
    test_num = rates[int(len(rates) / 2) - 1]
    test_rate = test_num/10000.0
    if test_num == 10000:
        print("It is not possible to pay the down payment in three years.")
        return 0

    # See how much savings come from this rate
    test_savings = get_savings(month_count, annual_salary, semi_annual_raise, test_rate, current_savings, r)
    steps += 1
    
    # If savings aren't within $100 of down payment
    if (abs(down_payment_cost - test_savings) > 100):
        half_rates = int(len(rates) / 2)
        # Remove half the list and re-check
        if (test_savings > down_payment_cost):
            del rates[half_rates:len(rates)]
            check(rates, month_count, annual_salary, semi_annual_raise, current_savings, r, down_payment_cost, steps)
        else:
            del rates[0:half_rates]
            check(rates, month_count, annual_salary, semi_annual_raise, current_savings, r, down_payment_cost, steps)
    else:
        print("Best savings rate:", test_rate)
        print("Steps in bisection search:", steps)

def get_savings(month_count, annual_salary, semi_annual_raise, test_rate, current_savings, r):
    while month_count <= 35:
        # Increase salary every 6 months
        if month_count > 0 and (month_count % 6) == 0:
            annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_addition = monthly_salary * test_rate
        # First month won't gain any interest
        if month_count >= 1:
            monthly_interest = current_savings * r / 12
            current_savings += monthly_interest
        current_savings += monthly_addition
        month_count += 1
    return current_savings



main()