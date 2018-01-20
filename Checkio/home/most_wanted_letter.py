'''
Created on 2018. 1. 20.

@author: jihye
'''
#실패
def checkio(text):

    #replace this for solution

    max_n=0
    text=text.lower()                    # 모두 소문자 
    most=text[0]                         # 초기화 값을 문자열의 첫 원

    for i in text:                       # 문자열 원소 반복  
        if i.isalpha():                  # 문자만 
            if text.count(i)>max_n:      # 갯수가 max_n보다 클때 
                most=i                   # most 는 해당 원
                max_n=text.count(i)      # max_n 은 해당 갯
            elif text.count(i) == max_n: # 갯수가 max_n 과 같을 때
                if i < most :            # most가 해당원소보다 클때, 문자 값 비교 
                    most=i               # most 는 i
                    max_n=text.count(i)  # max_n는 i의 갯수 
                
    
    
    return most
    
    #opertor.itemgetter(1) : value 정렬
    #opertor.itemgetter(0) : key 정렬 

print(checkio("One"))
print(checkio("AAaooo!!!!"))
print(checkio("Hello World!"))