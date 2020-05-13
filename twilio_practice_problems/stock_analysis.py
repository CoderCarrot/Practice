# 2. Stock Analysis

# In data analysis, the eliminate algorithm determines the single final value to use for each data parameter.
# The eliminate algorithm works in the following way:

#     Data is acquired from multiple sources in order from least to most preferred, i.e. If a parameter Pi is present in both source 1 and source 2, 
#     the parameter from the higher priority source, source 2, is used in the final parameter list, and any value from an earlier source is superseded.
#     As new parameters arrive, they are added to the list.
#     If a parameter Pi is present only in one of the sources, it is directly added to the final parameter list. Hence,
#     The result of performing the above operations until all the parameters from source 1 and source 2 are exhausted is the result of Eliminate-algorithm(source 1, source 2).
#     Each time a new value for a parameter is encountered from a higher preferred site, the old data is superseded.
#     Assuming three sources S1, S2, and S3.
#         Eliminate-algorithm(S1, S2, S3) = Eliminate-algorithm(Eliminate-algorithm(S1, S2), S3)

# Given a list of sources S1, S2, ..., Sn, find the final parameter list given by Eliminate-algorithm(S1, S2, .., Sn). Maintain your result in the order a key was first encountered.

# For example, a rating parameter of buy, sell or hold from three sources in increasing order of preference: 
# [buy, sell, hold], where buy is from S1, immediately superseded by sell S2, immediately superseded by hold S3.
# The final rating is the only one that hasn't been superseded, so you use "hold" as the final rating.

# Function Description: Complete the function computeParameterValue in the editor below.
# The function must return an array of strings that denotes the final parameter list values in the order their keys were first encountered.

# computeParameterValue has following parameter(s): sources: A 2-dimensional array of key:value pairs, each row is one source's data, sources presented from lowest to highest preference.

# Constraints:

#     1 <= n < 100
#     1 <= p < 1000

# Input Format for Custom Testing

#     The first line contains a positive integer n, the number of sources.
#     The next line contains a positive integer p, denoting the number of parameters of each source.
#     Each of the next n lines contains an array of p space-separated strings of format key:value, denoting the key and value of source[i] parameters.

# Input

# Sample Input 0:
# 2
# 3
# P1:a P3:b P5:x
# P1:b P2:q P5:x

# Sample Output 0:
# b
# b
# x
# q

# Explanation 0:
# Final parameter list:
# - P1 b (Source 2)
# - P3 b (Source 1)
# - P5 x (Source 2)
# - P2 q (Source 2)  

# input: sources?
# output: array of strings - final parameter list values in order 1st encountered

# Notes:
#     Sources are hash maps like? - Not really
#     each row = source
#     source ordered from low to high preference
#     # of sources is non zero and below 100
#     # of parameters in source is non zero and below 1000
#     parameters are space-separated in format "key:value"

# Thoughts:
#     How do you have an array that is space separated strings?
#         I'm going to assume that the actual input is an array of strings
#     I don't remember how to account for unlimited, optional arguments. Time to google.

#     I can keep the order they appear in a list... but then how do I override? 
#     I can override in a dictionary easily, but dictionaries are not supposed to be ordered.
#     Can I use a set somehow for easy lookup? They are also not ordered.
#     Maybe I can put them in speparate lists. 
#     Either way I think I need to reformat, somehow. 
#     What so I need from the first element?
#         I need the key:value pair for later comparison. 
#         I need to know I saw it first in case it comes up again. 
#         A very inefficient way would be to use a list and "in" so I'm going to do that to get a working solution first. 
#     How do I remove the key from the order list and move it if I can't find it by looking it up?
#         I can use splice to check if it's further in the list. 
#     I can't do & for the if statement to prevent repeating because the dictionary key value pair will not exist yet for the 2nd check.
#         I could do or! Maybe

# Human solution:
#     Write down the key value pairs when they appear and replace the value for the appropriate key when a new one is seen. 
#     Take all of the values in order written and write provide only those. 

# ['P1:a', 'P3:b', 'P5:x']

def compute_parameter_value(*sources):

    current_values = {}
    order_seen = []
    values = []

    for source in sources:
        for parameter in source:
            # print(parameter)
            parameter = parameter.split(':')
            # print(parameter)
            if (parameter[0] not in order_seen) or (parameter[1] != current_values[parameter[0]]):
                order_seen.append(parameter[0])
                # print(order_seen)
            current_values[parameter[0]] = parameter[1]
            # print(current_values)
    
    splice_helper = 1

    for key in order_seen:
        # print(key)
        if key not in order_seen[splice_helper:]:
            values.append(current_values[key])
        splice_helper += 1
    
    return values


# Time: 43 mins

print(compute_parameter_value(['P1:a', 'P3:b', 'P5:x'], ['P1:b', 'P2:q', 'P5:x']))

# Testing notes:
#   Forgot .split returns instead of changing in place. Which makes sense since strings are immutable.
#   Accidentally had the splice_helper in the if statement
#   The order the KEYS were first encountered! *facepalm* So much simpler. 

def compute_parameter_value2(*sources):

    current_values = {}
    order_seen = []
    values = []

    for source in sources:
        for parameter in source:
            parameter = parameter.split(':')
            if (parameter[0] not in order_seen):
                order_seen.append(parameter[0])
            current_values[parameter[0]] = parameter[1]

    for key in order_seen:
        values.append(current_values[key])

    return values

print(compute_parameter_value2(['P1:a', 'P3:b', 'P5:x'], ['P1:b', 'P2:q', 'P5:x']))

# Time Complexity: O(n*m^2) where n is number of sources and m is number of parameters per source. Either way, it's gross.
# Since dictionaries in python are now ordered, I don't actually need the order_seen list.
#   I could also just print the values for each key in the dictionaty instead of putting them in a list to then return.
#   Although this depends on the format desired for output.
# I can not think of a way to unpack the input without using 2 for loops.