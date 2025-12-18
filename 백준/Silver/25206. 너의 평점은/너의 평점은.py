import sys

sum_time = 0
time_grade = 0
d = {"A+": 4.5, "A0":4.0, "B+": 3.5, "B0": 3.0, "C+":2.5,
     "C0":2.0, "D+":1.5, "D0": 1.0, "F": 0.0     
     }
for _ in range (20) :
    subject,time,grade = map(str, sys.stdin.readline().split())
    int_time = int(time[0])


    if grade == 'P' :
        continue
    else :
        sum_time = sum_time + int_time
        time_grade = time_grade + (int_time * d[grade])
       




print(round((time_grade / sum_time),6))

    