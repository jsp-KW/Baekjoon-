import sys

N, M = map(int,sys.stdin.readline().split())
all_students= []
for i in range (N) :
    students = list(map(int,sys.stdin.readline().split()))
    for s in students:
        all_students.append((s,i))

all_students.sort()
current_classes= 0 

left = 0
min_val = float('inf')
cnt_dict = {}
for right in range (len(all_students)) :
    score_r, class_r = all_students[right]


    if class_r not in cnt_dict or cnt_dict[class_r] == 0 :
        current_classes +=1
        cnt_dict[class_r] =1
    else :
        cnt_dict[class_r] +=1

    while current_classes == N :
        
        score_l, class_l = all_students[left]
        difference = score_r - score_l # 최대 - 최소 차이 구하기
        if difference  < min_val :
            min_val =difference
        
        cnt_dict[class_l] -=1
        if cnt_dict[class_l] == 0 :
            current_classes -=1
        
        left+=1

print(min_val)

