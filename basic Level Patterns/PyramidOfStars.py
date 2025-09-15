a = 5
for i in range(1,a+1):
    for j in range((a+1)-i-1):
        print(" " ,end=" ")
    for star in range(2 * i - 1):
        print("*",end= " ")
    print()