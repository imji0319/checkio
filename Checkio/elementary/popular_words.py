'''
Created on 2018. 1. 18.

@author: jihye
'''
def popular_words(text, words):
    # your code here
    dic={}
    text=text.lower()  # 소문자로 변경 -> 대소문자 무시하기 위
    for i in words:
        
        dic[i]=text.count(i)
    
    
    return dic


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

