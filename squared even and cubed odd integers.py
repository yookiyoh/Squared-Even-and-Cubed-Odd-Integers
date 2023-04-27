# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 4 - Problem 4
# This program writes a method in Python wherein the extracted even integers will be squared 
# and the extracted odd integers will be cubed from the main text file 
# (similar acquisition from Program 1 where extraction of odd and even integers take place)
# Thus transferred into separate text files per each categorical result.

import time
import pyfiglet
from colorama import Fore, Style
from tqdm import tqdm

def user_input():
    # open the integers.txt file in write mode
    with open("integers.txt", "w") as input_file:
        
        # use of while looping
        while True:
            try:
                # asking the user for a number input
                user_input = int(input("Enter a number: "))  
                # check if the input is an integer
                if user_input <= 0 or user_input >= 0:
                    # user input will be written to integers.txt file
                    input_file.write(str(user_input) + '\n')
                    continue
            
            # if not, break out of the loop
            except ValueError:
                print("[Proceeding to exit the program...]")
                break

def main():
    # open the integers.txt file in read mode, double.txt file in write mode, triple.txt in write mode
    with open("integers.txt", "r") as input_file1, open("double.txt", "w") as even_squared1, open("triple.txt", "w") as odd_cubed1:

        # read integers.txt per line
        for line in input_file1:

            # convert inputs from integers.txt into integers
            int_inputs = int(line)

            # if the inputted integer is even
            if int_inputs % 2 == 0:

                # inputted integer will be squared
                squared_even = int_inputs ** 2

                # squared even integers will be inputted to double.txt file
                even_squared1.write(str(squared_even) + "\n")

            # if the inputted integer is odd
            elif int_inputs % 2 == 1:

                # inputted integer will be cubed
                cubed_odd = int_inputs ** 3

                # cubed odd integers will be inputted to triple.txt file
                odd_cubed1.write(str(cubed_odd) + "\n")

def outro():
    # print a goodbye message and terminate the program
    print("\nThank you for using this program!")
    print("Program terminating in...")
    exit()



# initialize
user_input()
main()
outro()