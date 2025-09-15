n = 5  # number of rows

for i in range(n):
    # Print leading spaces for pyramid shape
    print(" " * (n - i), end="")

    num = 1  # first number in every row is 1

    # Print values in row
    for j in range(i + 1):
        print(num, end=" ")

        # Update num using nCr formula relation
        num = num * (i - j) // (j + 1)
        print("number is",num)

    print()  # move to next row
