import time

def main():

    options = ["1.1", "1.2", "1.3", "2.1", "2.2", "2.3"]

    print("\nWelcome to the edX problems!\n")
    time.sleep(0.5)

    while True:
        selection = input("Input the problem you'd like to see: ")

        if selection not in options:
            print("Invalid response :(\nTry again\n")
        else:
            if selection == "1.1":
                u1p1()
                break
            if selection == "1.2":
                u1p2()
                break
            if selection == "1.3":
                u1p3()
                break
            if selection == "2.1":
                u2p1()
                break

    

def u1p1():
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


def u1p2():
    # Assume s is a string of lower case characters.
    # Write a program that prints the number of times the string 
    # 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
    # then your program should print:
        # Number of times bob occurs is: 2

    s = "azcbobobegghakl"
    key = "bob"
    count = 0

    for i in range(len(s)):
        if s[i:i+2] == key[0:2]:
            count += 1
        i += 1

    print("Number of times bob occurs is:", count)

def u1p3():
    # Assume s is a string of lower case characters.
    # Write a program that prints the longest substring of 
    # s in which the letters occur in alphabetical order. 
    # For example, if s = 'azcbobobegghakl', then your program 
    # should print:
        # Longest substring in alphabetical order is: beggh
    # In the case of ties, print the first substring. 
    # For example, if s = 'abcbcd', then your program should print:
        # Longest substring in alphabetical order is: abc

    s = "azcbobobegghakl"
    longest = []
    count = 0
    i = -1
    j = 0

    while i < len(s) - 1 and count < len(s):
        count += 1
        chain = [s[i + 1]]
        while j < len(s) - 1:
            i += 1
            j += 1
            if len(chain) > len(longest):
                longest = chain
            if s[i] <= s[j]:
                chain.append(s[j])
                continue
            else:
                chain = []
                break

    print("Longest substring in alphabetical order is:", "".join(longest))


def u2p1():
    # Write a program to calculate the credit card balance 
    # after one year if a person only pays the minimum monthly 
    # payment required by the credit card company each month.

    # Variables
    balance = 484
    annual_interest_rate = 0.20
    monthly_payment_rate = 0.04

    # Calculated variables
    monthly_interest_rate = annual_interest_rate / 12.0

    for i in range(12):
        balance = balance * (1 + monthly_interest_rate)
        minimum_monthly_payment = monthly_payment_rate * balance
        balance = balance - minimum_monthly_payment
    
    print("Remaining balance:", round(balance, 2))



main()