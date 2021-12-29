# pattern 5


for i in range(5):
    for j in range(5):
        if j>=i:
            print("* ", end="")
        else:
            print(" ", end=" ")

    for k in range(5):
        if i>=k:
            print("* ",end=" ")
    print()