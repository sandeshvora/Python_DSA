# Pattern 1
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *


for i in range(5):
    for j in range(5):
        if i>=j:
            print("* ", end=" ")
    print()
