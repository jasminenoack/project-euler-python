"""Solution to Project Euler Problem 1."""

def solve(limit: int = 1000) -> int:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    running_total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            running_total += i
    return running_total


if __name__ == "__main__":
    print(solve())
