# Pattern 3
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(5):
    for j in range(5):
        if i+j>=4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()