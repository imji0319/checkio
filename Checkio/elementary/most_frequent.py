'''
Created on 2018. 1. 17.

@author: jihye
'''
#Input: a list of strings.
#Output: a string.


def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    most_fre=0
    most=""
    for i in data:
        if data.count(i)>=most_fre:   
            most=i
            most_fre=data.count(i)
            
    return most