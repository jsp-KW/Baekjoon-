import sys

info = []
goal_cnt = int(sys.stdin.readline())

for _ in range (goal_cnt) :
    team_num, time = map(str, sys.stdin.readline().split())
    minutes = int(time.split(":")[0])*60
    seconds = int(time.split(":")[1])
    time = minutes +seconds
    info.append((int(team_num), time))



prev_time = 0
total_time = 48*60

score_a =0
score_b = 0

a_time = 0
b_time = 0
for i in range (0,goal_cnt) :

    if score_a > score_b :
        a_time += info[i][1] - prev_time
    elif score_b > score_a :
        b_time += info[i][1] - prev_time

    if info[i][0] == 1 :
        score_a +=1
    else :
        score_b +=1

    prev_time = info[i][1]

if score_a > score_b :
    a_time +=  total_time- prev_time
elif score_b > score_a :
    b_time +=  total_time - prev_time

a =""

b= ""
if (a_time // 60) < 10 : 
    a +="0"+ str(a_time//60)+":" 
    if a_time %60  <10 :
        a+= "0"+str(a_time%60)
    else :
        a+= str(a_time%60)
else :
    a+= str(a_time//60)+":"
    if a_time%60 < 10 :
        a+= "0" + str(a_time%60)
    else:
        a+= str(a_time%60)


if (b_time // 60) < 10 : 
    b +="0"+ str(b_time//60)+":" 
    if b_time %60  <10 :
        b+= "0"+str(b_time%60)
    else :
        b+= str(b_time%60)
else :
    b+= str(b_time//60)+":" 
    
    if b_time %60  <10 :
        b+= "0"+str(b_time%60)
    else :
        b+= str(b_time%60)




        
print(a)
print(b)