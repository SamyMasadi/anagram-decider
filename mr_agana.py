# Author: Samy Masadi
# Assignment: Homework 1 - Anagram Algorithms
#
# This program will help a user determine whether two strings are anagrams.
# It utilizes two different determination methods: brute force and linear.
#
# The program will first prompt the user for the method type. Then it will ask
# for the two strings.
#
# Note: user input for strings has some validation--it
# will check whether the input is a valid number--but it currently does not
# check for case or remove whitespace and special characters. The program
# assumes input strings will contain only lowercase letters.
#
# Finally, it will determine whether the strings are
# anagrams utilizing the method selected.
#
# It will also print the time taken for each determination, so the user may
# compare the efficiency of the methods.
#
# The program will loop until the user selects the exit option.

import time     # Used for performance measurement

### Function Definitions ###

def toString(List): 
    return ''.join(List)

# Function to compare permutations of string to another string
# This function takes three parameters: 
# 1. String to permute
# 2. String to compare
# 3. Starting index of the string 
# 4. Ending index of the string.
# Return: Boolean value representing if a match (anagram) was found
def permute(a, b, l, r):
    if l==r: 
        return b == toString(a)
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            if permute(a, b, l+1, r):
                return True
            a[l], a[i] = a[i], a[l] # backtrack
        return False
  
# Permute and toString functions are contributed by Bhavya Jain of geeks for geeks (converted to Python 3.x by S. Mello-Stark
# Permute has been modified by Samy Masadi for use in the overall program

# Function to print the menu of options for the user.
def printMenu():
    print()
    print("Which method should I use?")
    print("1: Brute Force")
    print("2: Linear")
    print("3: Brute Force and Linear")
    print("4: Exit")

# Function that utilizes the brute force algorithm to determine anagrams.
# Takes two parameters:
# 1. String to permute
# 2. String to compare
# Prints its determination and the time taken.
def effAnaBF(s1, s2):
    print("Brute Force: I'll look through every possible anagram.")
    print("Here are your strings:")
    print(s1)
    print(s2)
    start = time.perf_counter() # Start measuring time performance
    length = len(s1)
    str_list = list(s1)
    if permute(str_list, string2, 0, length-1): # Brute force algorithm
        print("Yes, the strings are anagrams.")
    else:
        print("Nope, the strings are not anagrams.")
    end = time.perf_counter()   # End measuring time performance
    print("I needed {:7.6f} seconds to decide.".format(end - start))

# Function that tracks letter counts in a string for later comparison
# Takes one parameter:
# 1. String for counting occurrences of its letters
# Return: a list containing counts for each of the 26 letters in the alphabet
def letterCount(string):
    counts = [0] * 26       # Initialize list with zeros for each letter a-z
    for i in range(0, len(string)):
        ch = string[i:i+1]
        ind = ord(ch) - 97  # Index determined by difference of character's
            # ASCII value and base value of 'a'. It will ensure the list
            # maintains counts for letters in the correct a-z order.
        counts[ind] += 1    # Increment count of character in the appropriate
            # space in the counts list.
    return counts

# Function that utilizes the linear algorithm to determine anagrams.
# It will compare lists containing counts of the letters for each of
# two strings. Because the lists are expected to have the same a-z order for
# the counts, they are directly comparable. Thus a match or mismatch of letter
# counts between two strings can determine an anagram.
# Takes two parameters:
# 1. String, for counting its letters
# 2. Second string, for counting its letters
# Prints its determination and the time taken.
def effAnaBtr(s1, s2):
    print("Linear: I'll just count the letters and compare.")
    print("Here are your strings:")
    print(s1)
    print(s2)
    start = time.perf_counter() # Start performance measurement
    if letterCount(s1) == letterCount(s2):  # The linear algorithm: a direct
        # comparison of letter counts in a-z order.
        print("Yes, the strings are anagrams.")
    else:
        print("Nope, the strings are not anagrams.")
    end = time.perf_counter()   # End performance measurment
    print("I needed {:7.6f} seconds to decide.".format(end - start))

# Note: The idea for the linear algorithm came from interactivepython.org:
# http://interactivepython.org/courselib/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html
# The code implementation is by Samy Masadi.

### Main Program ###

print("Hi, I'm Mr. Agana, The Anagram Decider")
print()
print("I'll figure out whether your strings are anagrams!")

run = True
while run:
    printMenu()
    try:
        choice = (int)(input("Enter your selection number: "))
        print()
        if choice > 0 and choice < 4:
            string1 = input("Enter a string: ")
            string2 = input("Enter another string: ")
            print()
            if choice == 1:
                effAnaBF(string1, string2)
            if choice == 2:
                effAnaBtr(string1, string2)
            if choice == 3:
                effAnaBF(string1, string2)
                print()
                effAnaBtr(string1, string2)
        elif choice == 4:
            print("All right, see you later!")
            run = False # Exit the program
        else:           # Default for invalid int input
            print("Please enter a number between 1 and 4.")
    except ValueError:  # Input validation in case of non-int values
        print()
        print("Sorry, I couldn't understand your choice.")
        print("Please enter your choice as an integer.")
