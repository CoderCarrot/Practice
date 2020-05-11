# Given a string, find the largest word that has even length.

# input is string.
# largest word
#     only if it has an even length. 

# Check for even or odd length before checking for longest to prevent checking unecessary words.
# Separate the sentence by spaces.
# Assume there is no punctuation. (This would be a question if I had an audience)
# Keep track of the current longest word. 
# Return the largest word.
# Assume no blank input. (This would be a question if I had an audience)
# Assume no 2 words are the same length. (This would be a question if I had an audience)


def find_largest_even_word(the_string):

    words = the_string.split(' ')
    largest_word = 'z'

    for word in words:
        if (len(word) % 2 == 0) & (len(word) > len(largest_word)):
            largest_word = word

    return largest_word

# Time: 12 mins


# If looking for the length of the largest word:

def find_length_of_largest_even_word(the_string):

    words = the_string.split(' ')
    largest_word = 0

    for word in words:
        if (len(word) % 2 == 0) & (len(word) > largest_word):
            largest_word = len(word)

    return largest_word

print(find_largest_even_word('This is a random sentence for testingss'))
print(find_length_of_largest_even_word('This is a random sentence for testingss'))