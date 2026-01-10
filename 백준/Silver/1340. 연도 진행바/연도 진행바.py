import sys

dic = {
    'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,
    'July':31,'August':31,'September':30,'October':31,'November':30,'December':31
}

def yoon_year (y) :
    return (y%400 ==0) or (y%4==0 and y%100 != 0) 

inputs =list (map(str, sys.stdin.readline().split()))

Month = inputs[0]
Day  = int(inputs[1].replace(',',''))
Year = int(inputs[2])
Time = inputs[3].split(":")
Time_Hour = int( Time[0])
Time_Min = int (Time[1])


# 윤년 -> 2월 29일임

if yoon_year(Year) :
    dic['February'] = 29


# 1년 전체 분
total_min =(366* 1440 if yoon_year(Year) else 365* 1440)

months = ['January','February','March','April','May','June','July','August',
          'September','October','November','December']

day_count = 0
for i in range (0,len(months)) :
    if months[i] == Month :
        break

    day_count += dic[months[i]]

print ((((day_count*1440 )+ (Day-1) * 1440 + (Time_Hour*60) +Time_Min  ) / total_min)* 100)


