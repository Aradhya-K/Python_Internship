def nth_largest(A,n):

    A_sorted = sorted(A, reverse=True)

    return A_sorted[n-1]

A = [19, 78, 67, 90, 56, 1]
n = 1


print(f"the {n}th largest number in the list is {nth_largest(A,n)}.")
