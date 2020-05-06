def one_away(word1, word2):

    count = 0
    difference = 0
    length1 = len(word1)
    length2 = len(word2)

    if (abs(length1 - length2) <= 1):
        while (count < length1) & (count < length2) & (difference < 2):
            if word1[count] != word2[count]:
                count += 1
                difference += 1
            else:
                count += 1
        
        if (difference == 1) & (abs(length1 - length2) == 0):
            return True
        elif difference == 0:
            return True

    return False


#Test Cases
print(one_away('make', 'fake')) #True
print(one_away('task', 'take')) #False
print(one_away('ask', 'asks')) #True
print(one_away('asks', 'ask')) #True
print(one_away('form', 'format')) #False
print(one_away('ask', 'asta'))  #False
print(one_away('task', 'ask'))  #True
    # This last one won't work with this code. Fix it.