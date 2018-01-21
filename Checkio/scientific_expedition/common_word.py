'''
Created on 2018. 1. 21.

@author: jihye
'''
def checkio(first, second):
    first=first.split(',')
    second=second.split(',')
    common=[]
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i]==second[j]:
                common.append(second[j])
    common=sorted(common)     # sorted : 원소 정렬 
    common=",".join(common)   # join : 리스트 원소 -> 문자열로 결합  
    
    
    
    print( common )
    
    
checkio("hello,world", "hello,earth")
checkio("one,two,three", "four,five,one,two,six,three")


