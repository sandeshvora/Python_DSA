# Python3 program to find permutation
# of n which is divisible by 3 but
# not divisible by 6
from math import log10, ceil, pow


# Function to find the permutation
def findPermutation(n):
    # length of integer
    len = ceil(log10(n))
    print(len)
    for i in range(0, len, 1):

        # if integer is odd
        if n % 2 != 0:

            # return odd integer
            return n
        else:

            # rotate integer
            n = ((n // 10) + (n % 10) *
                 pow(10, len - i - 1))
            continue

    # return -1 in case no required
    # permutation exists
    return -1


# Driver Code
if __name__ == '__main__':
    n = 132

    print(int(findPermutation(n)))

# This code is contributed
# by Surendra_Gangwar
