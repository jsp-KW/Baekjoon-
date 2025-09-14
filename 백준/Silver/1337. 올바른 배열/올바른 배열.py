import sys


n = int (sys.stdin.readline())
arr = []

for i in range (n) :
    num = int(sys.stdin.readline())
    arr.append(num)


arr.sort()
answer = 5


for i in range (n) :
    start = arr[i]
    end = start +4
    cnt = 0

    for j in range (i, n) :
        if arr[j] <= end :
            cnt +=1

        else :
            break
    answer = min (answer, 5-cnt)

print (answer)