import time

def main():
    print("\nWelcome to the edX problems!\n")
    time.sleep(0.5)

    while True:
        try:
            selection = int(input("Input the problem you'd like to see: "))
        except (ValueError):
            print("Please enter a number.")
            continue

        if (selection > 6) or (selection < 1):
            print("Invalid response :(\nproblems start at 1 and end at 10.\nPlease input a number from 1-10.\n")
        else:
            if selection == 1:
                p1()
                break
            if selection == 2:
                p2()
                break

    

def p1():
    # Assume s is a string of lower case characters.
    # Write a program that counts up the number of vowels contained 
    # in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
    # For example, if s = 'azcbobobegghakl', your program should print:
    # Number of vowels: 5

    s = "azcbobobegghakl"
    vowels = "aeiou"
    count = 0

    for char in s:
        for c in vowels:
            if char == c:
                count += 1
                break
    print("Number of vowels:", count)


def p2():
    # Assume s is a string of lower case characters.
    # Write a program that prints the number of times the string 
    # 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
    # then your program should print:
    # Number of times bob occurs is: 2

    s = "azcbobobegghakl"
    key = "bob"
    count = 0
    i = 0

    while i < len(s):
        if s[i:i+2] == key[0:2]:
            count += 1
        i += 1

    print("Number of times bob occurs is:", count)

main()