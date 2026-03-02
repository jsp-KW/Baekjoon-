import sys

S = int(sys.stdin.readline())

temp = 0
cnt = 0
for i in range (1,100000) :
    temp = temp +i
    if temp > S :
        break

    cnt +=1

print(cnt )