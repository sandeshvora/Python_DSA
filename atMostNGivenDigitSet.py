def atMostNGivenDigitSet(D, N):
    N = str(N)
    n = len(N)
    res = sum(len(D) ** i for i in range(1, n))
    i = 0
    while i < len(N):
        res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
        if N[i] not in D:
            break
        i += 1
    return res + (i == n)


D=["1","3","5","7"]
N=7000
print(atMostNGivenDigitSet(D,N))