'''
Created on 2018. 1. 17.

@author: jihye
'''
#Input: A tuple, at least 3 elements long.
#Output: A tuple.

def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here
    pack=[]
    pack.append(elements[0])
    pack.append(elements[2])
    pack.append(elements[-2])
    pack=tuple(pack)
    
    return pack


