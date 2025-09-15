n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" " , end = " ")
    for j in range(2 * i - 1):
        # First star, last star of row, or last row (to make it solid at bottom)
        if j == 0 or j == 2 * i - 2 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
