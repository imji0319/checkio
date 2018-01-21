'''
Created on 2018. 1. 21.

@author: jihye
'''

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    
    count=0   # 문자열이 없을 경우 존재 
    if len(line)>0:
        count=1

    for i in range(len(line)-1):
        if line[i]==line[i+1]:
            if line.count(line[i],i) > count:  #count( 찾는 문자 ,시작 지점 , 끝 지점 )
                count=line.count(line[i],i)
            
            
    return count      

    
print(long_repeat('sdsffffse'))
print(long_repeat('ddvvrwwwrggg'))
print(long_repeat("abababaab"))
print(long_repeat("abababa"))
