#Prompt:
# Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴

# You can assume the input string only contains lowercase letters.

# Examples:

#     "civic" should return True
#     "ivicc" should return True
#     "civil" should return False
#     "livci" should return False

# Possible Questions for Interviewer:
#   Does case matter? (Already answered)
#   Will there be any punctuation? (Techinically answered)
#   Will it be a continuous string of letters or will there be spaces? (Technically answered)
#   Will there be any letters occurring more than twice? (Implied answer based on solution)


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    
    letter_count_1 = {}
    letter_count_2 = {}
    
    for letter in the_string:
        if letter in letter_count_1:
            if letter in letter_count_2:
                if letter_count_1[letter] > letter_count_2[letter]:
                    letter_count_2[letter] += 1
                else:
                    letter_count_1[letter] += 1
            else:
                letter_count_2[letter] = 1
        else:
            letter_count_1[letter] = 1

    return abs(len(letter_count_1) - len(letter_count_2)) < 2

# Although this code passed the tests for the prompt, it will not pass if there is an even number of letters, with only one occurance of one unique letter and a 3rd occurance of another unique letter.
# This could be resolved by checking if string is len even or odd and then having extra tests for even-lengthed strings, but that would involve also comparing all of the keys in the dictionaries,
# which is highly inefficient at longer inputs with many unique letters.
# This solution is O(n) time.

# InterviewCake Solution:

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1

# My other idea was a similar solution to this one, except it has the same problems with letters that are repeated more than once.
# I do not feel like this is a comprehensive solution. 