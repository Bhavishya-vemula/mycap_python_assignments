# This Python program prints all positive numbers in a range.

# Define the start and end of the range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Iterate over the range and print all positive numbers.
for i in range(start, end + 1):
    if i >= 0:
        print(i)