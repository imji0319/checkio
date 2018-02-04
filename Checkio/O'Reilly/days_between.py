'''
Created on 2018. 2. 4.

@author: jihye
'''
import datetime


def days_diff(date1, date2):
    date1=datetime.date(date1[0],date1[1],date1[2])
    date2=datetime.date(date2[0],date2[1],date2[2])
    diff=abs(date1-date2)
    return diff.days
    
    

'''datetime : 시간데이터 패키지
-> date함수를 사용해 데이터유형을시간의 형태로 바꾸고 계산할 경우 
return 값 역시 date타입이기 때문에 그 값만 가져오기 위해 days 라는 함수 사용 
'''