import sys

# Purpose: Reads a file specified by the user, sums pairs of float numbers from each line,
#          and prints the cumulative sum after each line.
# Input: `filename` - a string representing the name of a text file, passed as a command-line argument.
# Output: Prints the cumulative sum of each pair of floats in the file. Prints an error message if
#         a line doesn’t contain exactly 2 numbers, if values aren't valid floats, or if the file doesn't exist.
# Data Representation: The file contains lines with two numbers (space-separated), which are summed per line.
filename = sys.argv[1]
total=0.0
try:
    with open(filename, "r") as file:
        for line in file:
            values=line.split()
            if len(values)!=2:
                continue
            try:
                num1=float(values[0])
                num2=float(values[1])
                total+=num1+num2
                print(f"Current sum: {total}")
            except ValueError:
                print("Missing or Not a number")
except FileNotFoundError:
    print("Please enter a valid file name.")
    exit()

