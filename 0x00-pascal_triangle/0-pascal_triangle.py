#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascals triangle of n
    """
    # Return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the result list with the first row [1]
    result = [[1]]

    # Loop through each row starting from the second row
    for i in range(1, n):
        # Create a new row based on the previous row
        row = [1]  # Start the row with 1

        # Add the middle values to the row
        for j in range(1, i):
            row.append(result[i - 1][j - 1] + result[i - 1][j])

        # End the row with 1
        row.append(1)

        # Add the new row to the result
        result.append(row)

    return result
