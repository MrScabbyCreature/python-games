"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    list2 = list(list1)
    for num in range(len(list1) -1, 0, -1):
        if list2[num] <= list2[num-1]:
            list2.pop(num)
    return list2
                
def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    listy = []
    for item in list1:
        if item in list2:
            listy.append(item)
    return remove_duplicates(listy)

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    new_list = []
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    num1 = num2 = 0
    len1 = len(list1)
    len2 = len(list2)
    while num1 < len1 and num2 < len2:
        if list1[num1] < list2[num2]:
            new_list.append(list1[num1])
            num1 += 1
        else:
            new_list.append(list2[num2])
            num2 += 1
        if num1 == len1:
            for num in range(num2, len2):
                new_list.append(list2[num])
        if num2 == len2:
            for num in range(num1, len1):
                new_list.append(list1[num])
    return new_list
        
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) == 1 or len(list1) == 0:
        return list1
    else:
        list2 = merge_sort(list1[:int(len(list1)/2)])
        list3 = merge_sort(list1[int(len(list1)/2):])
        list1 = merge(list2, list3)
        return list1
                           
        

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return ['']
    if len(word) == 1:
        return ['', word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        next_strings = []
        for string in rest_strings:
            if string != '':
                next_strings.append(first + string)
            next_strings.append(string + first)
            if len(string) > 1:
                for index in range(1, len(string)):
                    next_strings.append(string[:index] + first + string[index:])
        return rest_strings + next_strings
        
        
# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    my_list = []
    for line in netfile.readlines():
        my_list.append(line[:-1])
    return my_list
       

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
#run()
#a = gen_all_strings('abc')
#b = merge_sort(a)
#print a
print remove_duplicates([1, 3, 3, 8])
