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
            if selection == 3:
                p3()
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

    for i in range(len(s)):
        if s[i:i+2] == key[0:2]:
            count += 1
        i += 1

    print("Number of times bob occurs is:", count)

def p3():
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


main()