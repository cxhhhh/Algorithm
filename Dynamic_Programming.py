"""
Q2: Repurposing Underused Workspace (Dynamic Programming)
"""
import math


def select_sections(matrix):
    """
    Function description: To identify the list of locations (i, j) for n sections which has the lowest total occupancy rate

    Precondition: Valid input, matrix is the list of list with n rows and m columns,
                  matrix[i][j] is an integer number between 0 and 100 (inclusive)
    Postcondition: The list of locations (i, j) for n sections which has the lowest total occupancy rate is identified
                   minimum_total_occupancy and sections_location are returned in a list

    Input:
        matrix: a matrix of n rows and m aisles/columns, which contains the occupancy probability values
                for a total of nm sections
    Return:
        minimum: a list contains minimum_total_occupancy and sections_location
                 minimum_total_occupancy: an integer, which is total occupancy for the selected n sections to be removed
                 sections_location: a list of n tuples in the form of (i, j)
                                    Represent the location of one section selected for removal

    Time complexity:
        Best: O(nm), n is the number of rows, and m is the number of aisles/columns
        Worst: O(nm), n is the number of rows, and m is the number of aisles/columns
    Space complexity:
        Input: O(1)
        Aux: O(nm), n is the number of rows, and m is the number of aisles/columns

    References: Referred to the week 7 tutorial video
    """
    m = len(matrix[0])
    n = len(matrix)
    # Declare a memo, the format is to save the minimum occupancy and the path into a list
    memo = [[[0, []] for j in range(m)] for i in range(n + 1)]

    # Start from the second row, the elements in the first row are 0
    for i in range(1, n + 1):
        for j in range(m):
            # This is to go up, the first index is minimum occupancy, second index is the path
            # Updating go_up, go_left_diagonal and go_right_diagonal are the same format but different direction
            # Since memo has additional first row, so need to get i-1 from matrix
            # The path is always the previous path and add the current location
            go_up = [matrix[i - 1][j] + memo[i - 1][j][0], memo[i - 1][j][1] + [(i - 1, j)]]

            # Declare go_left_diagonal and go_right_diagonal
            go_left_diagonal = [math.inf, (math.inf, math.inf)]
            go_right_diagonal = [math.inf, (math.inf, math.inf)]
            # When it is valid to go to the left diagonal
            if j > 0:
                go_left_diagonal = [matrix[i - 1][j] + memo[i - 1][j - 1][0], memo[i - 1][j - 1][1] + [(i - 1, j)]]
            # When it is valid to go to the right diagonal
            if j < m - 1:
                go_right_diagonal = [matrix[i - 1][j] + memo[i - 1][j + 1][0], memo[i - 1][j + 1][1] + [(i - 1, j)]]
            # Update the current location with the minimum occupancy
            memo[i][j] = min(go_up, min(go_left_diagonal, go_right_diagonal))

    # Get minimum_total_occupancy and sections_location
    minimum = min(memo[n])
    return minimum

# ---------------------------------------------------------------------------
# --------------------------------- Testing ---------------------------------
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    occupancy_probability = [
        [31, 54, 94, 34, 12],
        [26, 25, 24, 16, 87],
        [39, 74, 50, 13, 82],
        [42, 20, 81, 21, 52],
        [30, 43, 19, 5, 47],
        [37, 59, 70, 28, 15],
        [2, 16, 14, 57, 49],
        [22, 38, 9, 19, 99]]

    print("\nQuestion 2:")
    print(select_sections(occupancy_probability))
