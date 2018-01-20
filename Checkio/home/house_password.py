'''
Created on 2018. 1. 20.

@author: jihye
'''
def checkio(data):

    #replace this for solution
    import re
    # 패턴 지정 
    num= re.compile("[0-9]+")   
    Up=re.compile("[A-Z]+")
    Low=re.compile("[a-z]+")
    
    # 패턴 검색 ->없으면 None
    num2=re.search(num,data)    
    Up2=re.search(Up,data)
    Low2=re.search(Low,data)
    
    if len(data)>=10 and num2 != None and Up2 != None and Low2 != None:
            return True
    else:
        return False
    
    
print(checkio('A1213pokl'))
print(checkio('asasasasasasasaas'))