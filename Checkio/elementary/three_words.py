'''
Created on 2018. 1. 16.

@author: jihye
'''
#세 개 이상의 문자가 연속되어 잇으면 true
def checkio(words):
    i = 0
    # 3개 이상 문자 연속 
    for word in words.split():
        if word.isalpha():
            i += 1
        else:
            i = 0
        if i == 3:
            return True
    
    return False
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


