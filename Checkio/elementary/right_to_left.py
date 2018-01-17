'''
Created on 2018. 1. 15.

@author: jihye
'''
def left_join(phrases):
    str1=(",".join(phrases)).replace("right","left")
    #"".join : 리스트나 배열값을 " "를 구분자로 하여 문자열로 만들기 
    #replace ( old, new ) : old -> new
    return str1
    
print(left_join(("left", "right", "left", "stop")))