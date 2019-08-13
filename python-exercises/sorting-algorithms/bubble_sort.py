"""
    File name: bubble_sort.py
    Author: Matthew Carter
    Date created: 06/03/2019
    Date last modified: 07/03/2019
    Python Version: 3.6.8
"""

import random
import timeit


# Function to create a random list of numbers given a list length and an upper limit for the numbers.
def create_random_no_list(value_upper_limit, list_length):
    return random.sample(range(value_upper_limit), list_length)


# Function to check if number list is fully sorted.
def sorted_check(unchecked_list):
    print("Checking...")
    for i in range(len(unchecked_list)-1):
        if unchecked_list[i] > unchecked_list[i+1]:
            # List is still not sorted.
            return False
    return True


# Bubble sort function.
def bubble_sort(unsorted_list):
    sorted_list_flag = False
    while not sorted_list_flag:
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                # Swap elements if latter is smaller.
                print("bubbling...swapping {} and {}".format(unsorted_list[i], unsorted_list[i+1]))
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i+1], unsorted_list[i]
                print(unsorted_list)
        # Check if list is fully sorted. If True exit while loop.
        sorted_list_flag = sorted_check(unsorted_list)
    print("Sorted list:\n{}".format(unsorted_list))


random_list = create_random_no_list(100, 10)
print(random_list)
bubble_sort(random_list)


##############################
# TIMING MY BUBBLE SORT CODE.

# print(timeit.timeit('''
# import random
#
#
# def create_random_no_list(value_upper_limit, list_length):
#     return random.sample(range(value_upper_limit), list_length)
#
#
# def sorted_check(unchecked_list):
#     for i in range(len(unchecked_list)-1):
#         if unchecked_list[i] > unchecked_list[i+1]:
#             # List is still not sorted.
#             return False
#     return True
#
#
# def bubble_sort(unsorted_list):
#     sorted_list_flag = False
#     while not sorted_list_flag:
#         for i in range(len(unsorted_list)-1):
#             if unsorted_list[i] > unsorted_list[i+1]:
#                 # Swap elements if latter is smaller.
#                 unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i+1], unsorted_list[i]
#         # Check if list is fully sorted. If True exit while loop.
#         sorted_list_flag = sorted_check(unsorted_list)
#     print(unsorted_list)
#
#
# random_list = create_random_no_list(100, 10)
# print(random_list)
# bubble_sort(random_list)
# ''', number=1000))

# It takes around 1.9 seconds to run my bubble sort code 1000 times on a ten number list (with print statements).
# It takes around 0.17 seconds to run my bubble sort code 1000 times on a ten number list (without non-essential
# print statements, using only two as with built-in approach below).


##############################
# TIMING BUILT-IN SORT FOR COMPARISON

# print(timeit.timeit('''
# import random
#
#
# def create_random_no_list(value_upper_limit, list_length):
#     return random.sample(range(value_upper_limit), list_length)
#
#
# random_list = create_random_no_list(100, 10)
# print(random_list)
# random_list.sort()
# print(random_list)
# ''', number=1000))

# It takes around 0.11 seconds to run the built-in sort method 1000 times on a ten number list.
