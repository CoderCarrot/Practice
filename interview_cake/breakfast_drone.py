
# Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.

# Each breakfast delivery is assigned a unique ID, a positive integer. 
# When one of the company's 100 drones takes off with a delivery, the delivery's ID is added to a list, delivery_id_confirmations. 
# When the drone comes back and lands, the ID is again added to the same list.

# After breakfast this morning there were only 99 drones on the tarmac. 
# One of the drones never made it back from a delivery. We suspect a secret agent from Amazon placed an order and stole one of our patented drones. 
# To track them down, we need to find their delivery ID.

# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

# The IDs are not guaranteed to be sorted or sequential. Orders aren't always fulfilled in the order they were received, and some deliveries get cancelled before takeoff.


# #################################################################################################################################################################################
# Problem:
#     Find unique integer in list of duplicate integers.

# Notes: 
#     IDs are not ordered.
#     IDs 1st added to the list after takeoff
#     IDs added to the list when return

# Questions:
#     What about order cancellations after takeoff?
#         Assume still added to the list since leaving and landing are what adds it to the list
#     Do IDs get added when orders are cancelled before drone leaves?
#         Assume ID does not get added since leaving and landing are what adds ID

# Thoughts:
#     Brute force would be to check every ID to see if there is a 2nd ID. Double loop. O(n^2) runtime.
#     Due to looking for a unique integer, I want to use sets, but I don't think that's the answer here.
#     If I use a counting algorithm to create a dictionary where the keys are the IDs and the values are the number of times they appear, I can then look for the key that has a value of 1.
#         This would involve looping once to create the dictionary and looping again to find the value we want since we don't know the key we want. This brings it down to O(2n) runtime. 
#         Can it be done in O(n)?
#     !!! I can add to the dictionary the first time an ID is seen and then remove from the dictionary when it is seen again. 
#         Since all drones come back, there should be an even number of duplicates, enabling this to leave one ID in the dictionary. 
#         Dictionary add and remove is constant due to constant lookup, making the runtime 0(n)! Space complexity is O(n)

def find_unique_id(delivery_ids):

    unique_ids = {}

    for id in delivery_ids:
        if id in unique_ids:
            unique_ids.pop(id)
        else:
            unique_ids[id] = 1

    unique_id = list(unique_ids.keys())

    return unique_id[0]

# Time: 20 mins


# O(n) time and O(1) space solution from interview cake:


def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:

        unique_delivery_id ^= delivery_id

    return unique_delivery_id

# Practicing what's happening on the lowest level:
# 010
# 101
# 111
# 100
# 011

# 0110
# 1011
# 1101