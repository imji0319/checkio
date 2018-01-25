'''
Created on 2018. 1. 25.

@author: jihye
'''
def verify_anagrams(first_word, second_word):
    set_first=sorted(list(first_word.lower().replace(" ","")))
    set_second=sorted(list(second_word.lower().replace(" ","")))

    if set_first==set_second:
        return True
    return False





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    
    
##ininstance() : 해당 값의 자료 형태를 비교할 때 사용     



