import time

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
        print("Thanks! input =", selection)
        break