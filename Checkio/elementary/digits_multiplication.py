'''
Created on 2018. 1. 15.

@author: jihye
'''
def checkio(number):
    
    num=str(number)
    mix=1
    for i in num:
        if i != "0":
            mix*=int(i)
    return mix

print(checkio(1000))