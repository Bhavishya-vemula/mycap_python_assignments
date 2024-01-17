# all positive numbers in a range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(start, end + 1):
    if i >= 0:
        print(i)
