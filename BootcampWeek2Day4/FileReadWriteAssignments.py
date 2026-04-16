file_name = 'textfile.txt'

line_count = 0

try:
    with open(file_name, 'r') as file:
        for line in file:
            print(line.strip().upper())
            line_count += 1
    print(f"\nTotal Number of Lines: {line_count}")

except FileNotFoundError:
    print(f"Error: The file '{file_name} was not found.")

"""
    EXPECTED OUTPUT:
    HI.  THIS IS MAY'S TEXTFILE.
    I AM CURRENTLY LEARNING MORE PYTHON PROGRAMMING.
    I AM ALSO LEARNING ABOUT HOW TO OPEN, CLOSE, READ, AND WRITE FILES.
    IN ADDITION, THIS IS ALL PART OF A BOOTCAMP.
    I ENJOY LEARNING ABOUT PYTHON PROGRAMMING.

    Total Number of Lines: 5
"""