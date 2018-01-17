'''
Created on 2018. 1. 15.

@author: jihye
'''

def index_power(array, n):
    
    if n<len(array):
        return array[n]**n
    else:
        return -1
    
print(index_power([1, 3, 10, 100], 3))