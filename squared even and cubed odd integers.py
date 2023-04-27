# Codilan, Ralph Lorenz I.
# BSCpE 1-5
# Object-Oriented Programming | Assignment 4 - Problem 4
# This program writes a method in Python wherein the extracted even integers will be squared 
# and the extracted odd integers will be cubed from the main text file 
# (similar acquisition from Program 1 where extraction of odd and even integers take place)
# Thus transferred into separate text files per each categorical result.

# open the integers.txt file in write mode
with open("integers.txt", "w") as file:
    
    # use of while looping
    while True:
        try:
            # asking the user for a number input
            int_input = input("Enter a number: ")
            
            # check if the input is an integer
            if int_input <= 0 or int_input >= 0:

            # user input will be written to integers.txt file
            int_input.write(str(int_input) + '\n')
            continue
        
        # if not, break out of the loop
        except:
            print("[An error occurred. Proceeding to exit the program...]")
            break

# open the integers.txt file in read mode
with open("integers.txt", "r") as file:
    
    # read all the lines in the integers.txt file and convert them into integers
    integers = [int(line.strip()) for line in file.readlines()]

# create empty lists for even and odd integers
even_integers = []
odd_integers = []

# sort the integers in ascending order

# iterate over the integers and extract even and odd integers

# if the acquired integer is even
   # square
   # squared even integers will be tranferred to double.txt

# if the acquired integer is odd
   # cube
   # cubed odd integers will be transferred to triple.txt

# open the double.txt file in write mode and write squared even integers to it

# open the triple.txt file in write mode and write cubed odd integers to it

# print a goodbye message and terminate the program