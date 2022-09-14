import time
import math

def main():
    print("\nWelcome to MIT's Intro to Python Course!\n")
    time.sleep(1)

    print("Here, you can find my responses to each pset.\n")
    time.sleep(1)

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



main()