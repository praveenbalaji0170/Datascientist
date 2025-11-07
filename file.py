# Ask user for file name
filename = input("Enter the file name: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()   # Read the entire text

        # Count how many characters are uppercase
        count = sum(1 for ch in content if ch.isupper())

        print("Total number of capital letters:", count)

except FileNotFoundError:
    print("File not found! Please check the file name.")
