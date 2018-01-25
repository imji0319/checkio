'''
Created on 2018. 1. 25.

@author: jihye
'''

def checkio(data):
    string=""
    string+='M'* (data//1000)

    if data%1000//100 < 4:
        string+='C'*(data%1000//100)
    elif data%1000//100 == 4:
        string+='CD'
    elif data%1000//100 <= 8:
        string+='D'+'C'*(data%1000//100-5)
    else:
        string+='CM'
        
    if data%1000%100//10 < 4:
        string+='X'*(data%100%100//10)
    elif data%1000%100//10 == 4:
        string+='XL'
    elif data%1000%100//10 <= 8:
        string+='L'+'X'*(data%1000%100//10-5)
    else:
        string+='XC'
        
    if data%1000%100%10 < 4:
        string+='I'*(data%1000%100%10)
    elif data%1000%100%10 == 4:
        string+='IV'
    elif data%1000%100%10 <= 8:
        string+='V'+'I'*(data%1000%100%10-5)
    else:
        string+='IX'
        
        

    print(string)
   
   
    
checkio(6)
checkio(499) 

#400 50 40 5 4
#CD L XL V IV
checkio(3888)
#3000 800 80 8
#MMM DCCC LXXX VIII
checkio(1850)