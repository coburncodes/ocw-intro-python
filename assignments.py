import time
import math

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


    else:
        print("Must enter A, B, or C")



main()