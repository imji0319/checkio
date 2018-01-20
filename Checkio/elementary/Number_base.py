'''
Created on 2018. 1. 20.

@author: jihye
'''
def checkio(str_numbers,radix):
    
    # 예외 처리 try - except error종류 
    try:
        return (int(str_numbers,radix))
    except ValueError:
        return -1 
    

        
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

