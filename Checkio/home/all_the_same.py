'''
Created on 2018. 2. 4.

@author: jihye
'''
from typing import List, Any
#typing 모듈은 표준 라이브러리에 포함되어 있음

def all_the_same(elements: List[Any]) -> bool:
    #all_the_same(elements: List[Any]) -> bool:
    # 인수 elements 는 list 형태 
    # 리턴은 bool 형태로 
    # 리스트 안의 값은 any 로 어떤 값이어도 가능 
    
    # your code here
    for i in range(len(elements)-1):
        if elements[i] != elements[i+1]:
            return False
        
    return True

