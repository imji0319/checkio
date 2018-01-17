'''
Created on 2018. 1. 15.

@author: jihye
'''
def find_message(text):
    """Find a secret message"""
    
    string=""
    for i in text:
        if i.isupper() :
            string+=i
           
    return string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


