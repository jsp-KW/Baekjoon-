import sys


N = int (sys.stdin.readline())

li = []
for _ in range (N):
    student = list(map(str,sys.stdin.readline().split()))
    li.append(student)

for i in range (N):
    li[i][1] = int(li[i][1])
    li[i][2] = int(li[i][2])
    li[i][3] = int(li[i][3])
    

li.sort(key= lambda x: (-x[1],x[2],-x[3],x[0]))

for l in li:
    print (l[0])