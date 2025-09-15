# Number Palindrome Pyramid in Python

n = 5  # number of rows

for i in range(1, n + 1):  # rows
    # Print leading spaces
    for space in range(n - i):
        print(" ", end="")

    # Print increasing numbers (1 to i)
    for j in range(1, i + 1):
        print(j, end="")

    # Print decreasing numbers (i-1 down to 1)
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()  # move to next line
