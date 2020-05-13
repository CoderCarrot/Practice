# 3. K-Subsequences

# We define a k-subsequence of an array as follows:

#     It is a subsequence of contiguous elements in the array, i.e. a subarray.
#     The sum of the subsequence's elements, s, is evenly divisible by k (i.i: s % k = 0).

# Given an array of integers, determine the number of k-subsequences it contains.
# For example k = 5 and the array nums = [5, 10, 11, 9, 5].
# The 10 k-subsequences are: {5}, {5, 10}, {5, 10, 11, 9}, {5, 10, 11, 9, 5}, {10}, {10, 11, 9}, {10, 11, 9, 5}, {11, 9}, {11, 9, 5}, {5}.

# Function Description: Complete the function kSub in the editor below.
# The function must return a long integer that represents the number of k-subsequences.

# kSub has following parameter(s):

#     k: an integer that the sum of the subsequence must be divisible by
#     nums[nums[0], ..., nums[n-1]]: an array of integers

# Constraints:

#     1 <= n <= 3 x 10^5
#     1 <= k <= 100
#     1 <= nums[i] <= 10^4

# Input Format for Custom Testing

#     The first line contains an integer k, the number the sum of the subsequence must be divisible by.
#     The next line contains an integer n, that denotes the number of elements in nums.
#     Each line i of the n subsequent lines (where 0 <= i < n) contains an integer that describes nums[i].

# Input

# Sample Input 0:
# 3
# 5
# 1
# 2
# 3
# 4
# 1

# Sample Output 0:
# 4

# Explanation 0:
# The 4 contiguous subsequences of nums having sums that are evenly divisible be k = 3 are:
# {3}, {1, 2}, {1, 2, 3}, {2, 3, 4}

# Input:
#     a list of integers
#     an integer
# Output:
#     a long integer (# of k-subs)
# Notes:
#     array has length greater than 0
#     k is a number inclusively between 1 and 100
#     integers in the array are non negative and non zero

# Human Solve:
#     Look for single elements and pairs first.
#     Start at beginning and continuously add and remove numbers until the sum is evenly divisible by k.
#     Brute force: start at first element, check each time you add an element. 
#         Start removing elements from the beginning when you reach the end of the array. Check each time you remove an element.
#         O(n^n) time for brute force?

# Thoughts:
# Don't optimize too early.
# Just get code that works first.
# While and for loop?
# pop off front to keep length variable
# could do this recursively
# can use while sequence instead of a counter (empty list is falsey)


def k_sub(sequence, k):

    num_k_sub = 0

    while sequence:
        to_sum = []
        for num in sequence:
            to_sum.append(num)
            if sum(to_sum) % k == 0:
                num_k_sub += 1
        sequence.pop(0)

    return num_k_sub


print(k_sub([5, 10, 11, 9, 5], 5))
print(k_sub([1, 2, 3, 4, 1], 3))

# Time: 30 mins, 35 after testing and fix.

# Testing notes:
#   Forgot to clear to_sum after popping from sequence

# The runtime on this makes me sad. Time to think of ways to optimize!
