'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# Plan -->
# Base case:
# If word is less than length of 2 than 'th' will not be present in this part of the string or a string that has a length of 1
# Count:
# To count we can add one to each of the result of the function call, when each function call gets returned, the number gets returned with it, then this gets added to previous function call until reach the first function, then we get the total count returned
# Recursive case
# we want to search 2 characters each call, from start to end of word
# If first two characters contain the 'phrase' then we keep recursion going checking for the next 2 characters (starting with second index) and add 1
# If it doesnt, we have another recursion case, where it checks the first index and second index with no +1 as no occurence of phrase


def count_th(word):

    # Case matters
    phrase = "th"

    # Base case
    if len(word) < 2:
        return 0

    if word[0:2] == phrase:
        # the next characters excluding the two we have sliced are passed into params
        return 1 + count_th(word[2:])

    if word[0:2] != phrase:
        return count_th(word[1:])
