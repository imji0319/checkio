'''
Created on 2019. 12. 29.

@author: jihye
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    #replace this for solution
    print("숫자", number)
    
    result = ""
    new_ten = ""
    
    
    if number < 10: # 10보다 작을 때
        result = FIRST_TEN[number-1]
        
    elif 10 <= number < 20 : # 10보다 크거나 같고 20보다 작을 때
        result = SECOND_TEN[number-10]

    elif number//10 in range(2,10) and number%10 == 0: # 10의 배수 일때
        result = OTHER_TENS[number//10-2]
        
    elif number%10 in range(1,10) and number < 100 : # 20보다 크지만 10의 배수가 아닐 때
        ten = number//10
        one = number-ten*10
        
        result = OTHER_TENS[ten-2] + " " + FIRST_TEN[one-1]
        
        
    elif number//100 in range(1,10): #100보다 클 때 

        hun = number//100
        print("100 : ", hun) 
        ten = number-hun*100
        print("10 : ", ten)
        one = number%100%10
        print("1 : ", one)
        
        result = FIRST_TEN[hun-1]+" "+HUNDRED
        
        #new_ten exist
        if ten >= 10 :
            n = ten//10
            if 10 <= ten < 20:
                new_ten = SECOND_TEN[ten-10]
                result = result + " " + new_ten
            
            elif ten//10 in range(2,10) and ten%10 == 0:
                new_ten = OTHER_TENS[n-2]
                result = result+" "+new_ten
                
            else: 
                new_ten = OTHER_TENS[n-2]
                result = result+" "+new_ten +" "+ FIRST_TEN[one-1]

        elif ten != 0 :
            result = result + " "+FIRST_TEN[ten-1]



    
        
    print(result)
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(999) == 'nine hundred ninety nine','7th example'
    assert checkio(88) == 'eighty eight','8th example'
    assert checkio(100) == 'one hundred','9th example'
    assert checkio(302) == 'three hundred two','10th example'
    assert checkio(940) == 'nine hundred forty','11th example'
    assert checkio(345) == 'three hundred forty five','12th example'
    assert checkio(38) == 'thirty eight','12th example'
    
    
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')