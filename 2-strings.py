# Given 2 strings S and T, return if they are equal when both are typed into
# empty text editors. # means a bachspace character.
# Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: True
# Explanation: Both S and T become "ac"

# Example 2:
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explaination: Both S and T become "".

# Example 3:
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".

# Example 4:
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

# Note:
# 1. 1<= S.length <= 200
# 2. 1 <= T.length <= 200
# 3. S and T only contain lowercase letters and '#' characters.

def are_two_strings_equal(S, T):
    # parse strings to see what they evaluate to:
    # put each letter into lists and remove when excountering #, but only if the list is not already empty
    # concatenate to compare string IDs (faster than comparing 2 lists?)
    parse1 = []
    parse2 = []

    for letter in S:
        if letter == '#':
            if parse1:
                parse1.pop()
        else:
            parse1.append(letter)

    