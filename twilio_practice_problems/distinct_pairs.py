# 1. Distinct Pairs

# In this challenge, you will be given an array of integers and a target value.
# Determine the number of distinct pairs of elements in the array that sum up to the target value.
# Two pairs (a, b) and (c, d) are considered to be distinct if and only if the values in sorted order do not match i.e. (1, 9) and (9, 1) are indistinct but (1, 9) and (9, 2) are distinct.

# For Example, given the array [1, 2, 3, 6, 7, 8, 9, 1] and a target value of 10, the seven pairs (1, 9), (2, 8), (3, 7), (8, 2), (9, 1), (9, 1) and (1, 9) all sum to 10 and there are only 
# three distinct pairs: (1, 9), (2, 8), and (3, 7).

# Function Description: Complete the function numberOfPairs in the editor below.
# The function must return an integer, the total number of distinct pairs of elements in the array that sum to the target value.

# numberOfPairs has the following parameter(s):

#     a[a[0], ..., a[n-1]]: an array of integers to select the pairs from.

# Constraints:

#     1 <= n <= 5 x 10^5
#     0 <= a[i] <= 10^9
#     0 <= k <= 5 x 10^9

# Input Format for Custom Testing

#     The first line contains an integer n, the size of the array a.
#     The next n lines each contain an element a[i] where 0 <= i < n.
#     The next line contains an integer k, the target value.

# Input Sample Input 0: 
# 6 
# 1 3 46 1 3 9 
# 47

# Sample Output 0:
# 1

# Explanation 0:
# a = [1, 3, 46, 1, 3, 9]
# There are 4 pairs of unique elements where a[i]+a[j] = k:

# 1. (a[0] = 1, a[2] = 46)
# 2. (a[2] = 46, a[0] = 1)
# 3. (a[2] = 46, a[3] = 1)
# 4. (a[3] = 1, a[2] = 46)
# In the list above, all four pairs contain the same values.  
# We only have 1 distinct pair (1, 46).

# Notes:
#     Input: 
#         array (list) of integers
#         target value
#     Objective:
#         # of distinvt pairs that sum to target value.
#     Return:
#         integer
#     General:
#         the length of the array is non zero
#         no negative numbers in the array
#         the target sum is non negative
#     Initial thoughts:
#         Since duplicate numbers will not matter for distinct pairs, I can use a set for fast lookup.
#             This will enable me to do the problem in O(n) time
#         I will need a counter to count distinct pairs as I loop through the array to check for the compliment of the current element via set lookup. 
#     Thoughts while writing problem:
#         I can avoid getting an inflated number by using the set for the loop also.
#             I will also have to divide by 2 to get the accurate number since both numbers will be seen.
#             This could also be solved by removing the seen numbers from the set.
#   Thoughts after testing:
#       The set doesn't work for even numbers that have the same number in there twice.
#       This was not a consideration in the problem description and would be a good question if a person were giving the interview.
#           If it's the same number, is it a pair? - Probaby because they are different elements of the array.
#       The current return is a float - easy fix.
#       How do I fix this?
#           I can sort the list and skip the next element if it is the same as the previous and still use a comparison set unless the number is the number/2.
#           I can avoid the sort and such in the case of odd numbers by checking if the target number first
#           I can save time by breaking after I reach k/2
#           I need a counter to index
#    Thoughts after 2nd test:
        # I forgot to account for if k/2 is not in the array and k is even.
        # I also mixed up the check for even and odd

def numberOfPairs(a, k):

    # Initiate counter
    num_of_pairs = 0
    array_to_set = set(a)

    if (k % 2) != 0:
        for num in array_to_set:
            if (k-num) in array_to_set:
                num_of_pairs += 1
    else:
        a.sort()
        counter = 1
        for num in a:
            if num != k / 2:
                if num != a[counter] & (k - num) in array_to_set:
                        num_of_pairs += 1
            else:
                if num == a[counter]:
                    num_of_pairs += 1
                break
            counter += 1

    return int(num_of_pairs/2)

# Solution after 45 mins. I will continue working below.


def numberOfPairs2(a, k):

    # Initiate counter
    num_of_pairs = 0
    array_to_set = set(a)

    if (k % 2) != 0:
        for num in array_to_set:
            if (k-num) in array_to_set:
                num_of_pairs += 1
    else:
        a.sort()

        counter = 1
        half_of_target = int(k / 2)

        for num in a:

            if num < half_of_target:

                if (num != a[counter]) & ((k - num) in array_to_set):
                    num_of_pairs += 1

            elif num == a[counter] & num == half_of_target:
                num_of_pairs += 1
                break

            elif num > half_of_target:
                break

            counter += 1

        return num_of_pairs

    return int(num_of_pairs/2)

# Took 30 more minutes to get a working solution due to order of operations and lack of sufficient parentheses.
# I would like to clean up this solution later. This is a mess and is no longer O(n).


print(numberOfPairs2([1, 3, 46, 1, 3, 9], 47))
print(numberOfPairs2([1, 3, 46, 1, 3, 9], 4))
print(numberOfPairs2([1, 3, 46, 2, 2, 9], 4))
print(numberOfPairs2([1, 2, 3, 6, 7, 8, 9, 1], 10))