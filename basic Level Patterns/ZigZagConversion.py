# Zig-Zag Pattern in Python

n = 9  # number of columns (width)

for i in range(1, 4):  # only 3 rows for zig-zag
    for j in range(1, n + 1):  # loop through columns

        # Condition for placing stars
        if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")

    print()  # move to next row
