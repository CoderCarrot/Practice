# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: [[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0],[0,0,0,0,0]]

# Output: 1

# [1,1,1,1,0]
# [1,1,0,1,0]
# [1,1,0,0,0]
# [0,0,0,0,0]

# Example 2:

# Input: [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]

# Output: 3

# [1, 1, 0, 0, 0]
# [1, 1, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 0, 1, 1]


def count_islands(grid_map):

    # Human Soln: stack them and see if there are 1's horizontally or vertically
    # Breakdown:
    #   check the 1st postion of the 1st set.
    #       if 0, move on to 2nd position in 1st set. - nope. will cause looking at a position twice.
    #       if 1, check 2nd position of 1st set.
    #           

    return island_number
