"""Solution to Project Euler Problem 1."""

def solve(limit: int = 1000) -> int:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    # total 3s
    count_3 = (limit - 1) // 3
    three_sum = 3 * count_3 * (count_3 + 1) // 2
    # total 5s
    count_5 = (limit - 1) // 5
    five_sum = 5 * count_5 * (count_5 + 1) // 2
    # total 15s (to avoid double counting)
    count_15 = (limit - 1) // 15
    fifteen_sum = 15 * count_15 * (count_15 + 1) // 2

    return three_sum + five_sum - fifteen_sum


if __name__ == "__main__":
    print(solve())
