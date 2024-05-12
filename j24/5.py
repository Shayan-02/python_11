def sum_of_series(m, n):
    """
    Calculates the sum of an arithmetic series with initial term m and n terms, where m and n are input by the user.

    Args:
        m (int): initial term
        n (int): number of terms

    Returns:
        int: The sum of the arithmetic series.
    """
    total = 0
    for i in range(n + 1):
        total += m + (i * m)
    return total


m = int(input("Enter the initial term(m): "))
n = int(input("Enter the number of terms(n): "))
result = sum_of_series(m, n)
print(f"The sum of the series for m={m} and n={n} is {result}")