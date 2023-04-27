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
        

# asking the user for input

# check if the input is an integer

# if not, break out of the loop

# write the integer to the file

# open the integers.txt file in read mode

# read all the lines in the integers.txt file and convert them into integers

# create empty lists for even and odd integers

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