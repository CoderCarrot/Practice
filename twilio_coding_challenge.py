# Given two strings, one is a subsequence if all of the elements of the
# first string occur in the same order within the second string. They do
# not have to be contiguous in the second string, but order must be
# maintained. For example, given the string 'I like cheese', the words ('I',
# 'cheese') are one possible subsequence of that string. Words are space
# delimited.
# Given two strings, s and t, where t is a subsequence of s, report the
# words of s, missing in t (case sensitive), in the order they are missing.
# Example
# s = 'I like cheese'
# t = 'like'
# Then 'like' is the subsequence, and ['I', 'cheese'] is the list of missing
# words, in order.
# Function Description
# Complete the function missingWords in the editor below.
# missingWords has the following parameter(s):
# string s: a sentence of space-separated words
# string t: a sentence of space-separated words
# Returns:
# string[i]: an array of strings that contains all words in s that are
# missing from t, in the order they occur within s
# Constraints
# Strings s and t consist of English alphabetic letters (i.e., a−z and
# A−Z), dash '-', and spaces only.
# All words are delimited by a space
# 1 ≤ |t| ≤ |s| ≤ 10
# 1 ≤ length of any word in s or t ≤ 15
# It is guaranteed that string t is a subsequence of string s.
# Input Format for Custom Testing
# Input from stdin will be processed as follows and passed to the
# function.
# The first line contains a string s.
# The first line contains a string t.
# Sample Case 
# Sample Input
# I am using HackerRank to improve programming →
# s = 'I am using HackerRank to improve
# programming'
# am HackerRank to improve →
# t = 'am HackerRank to improve'
# Sample Output
# I
# using
# programming
# Explanation
# The missing words are:
# 1. I
# 2. using
# 3. programming
# Add these words in order to the array ["I", "using", "programming"],
# then return this array as the answer.


def find_missing_words(s, t):

    missing_words = []
    index = 0

    s_list = s.split(' ')
    t_list = t.split(' ')

    for word in s_list:
        if index < len(t_list):
            if word == t_list[index]:
                index += 1
            elif (word != t_list[index]):
                missing_words.append(word)
        else:
            missing_words.append(word)

    return missing_words

s = 'I am using HackerRank to improve programming'
t = 'am HackerRank to improve'
print(find_missing_words(s, t))

w = 'I like cheese'
f = 'like'
print(find_missing_words(w, f))
