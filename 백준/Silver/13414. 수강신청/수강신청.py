import sys


K, L = map(int,sys.stdin.readline().split())

wating= set()
history = dict()
order= 1
for _ in range(L) :
    student_num = sys.stdin.readline().rstrip()
    if student_num not in wating:
        wating.add(student_num)
        history[student_num] =order
      
    else:
        history[student_num] = order

    order+=1

cnt= 0

list_his = []

for stu, order in history.items():
    list_his.append((stu, order))

list_his.sort(key= lambda x : (x[1]))

for tup in list_his:
    if cnt == K:
        break

    if tup[0] in wating :
        print(tup[0])
        cnt+=1


        
    

