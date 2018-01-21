'''
Created on 2018. 1. 21.

@author: jihye
'''

def checkio(game_result):
    
    g1=game_result[0]
    g2=game_result[1]
    g3=game_result[2]
    
    #가로줄 빙고 
    for i in game_result:
        if i[0]==i[1]==i[2]=='X':
            return('X')
        elif i[0]==i[1]==i[2]=='O':
            return('O')
    #세로줄 빙고 
    for i in range(3):
        if g1[i]==g2[i]==g3[i]:
            if g1[i]=='X':
                return ('X')
            elif g1[i]=='O':
                return('O')
            
    #대각선 빙고 
    if g1[0]==g2[1]==g3[2]:
        if g1[0]=='X':
            return ('X')
        elif g1[0]=='O':
            return('O')
    elif g1[2]==g2[1]==g3[0]:
        if g1[2]=='X':
            return ('X')
        elif g1[2]=='O':
            return('O')
    #노 빙고
    return 'D'
        

print(checkio([
        "X.O",
        "XX.",
        "XOO"]))
print(checkio([
        "O.X",
        "XX.",
        "XOO"]))

print(checkio([
        "OO.",
        "XOX",
        "XOX"]))

print(checkio([
        "OOX",
        "XXO",
        "OXX"]))
print(checkio([
        "OXO",
        "XXO",
        "XOX"]))
print(checkio([
        ".OX",
        ".XX",
        ".OO"]))


