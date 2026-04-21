import sys

T = int(sys.stdin.readline())
answers = []
for _ in range (T) :
    cnt = int(sys.stdin.readline())
    arr =list(map(int,sys.stdin.readline().split()))

    arr.sort()
    answer = -1
    for i in range (2,cnt) :
        if answer < arr[i] -arr[i-2]:
            answer = arr[i]-arr[i-2]
    answers.append(answer)

for ans in answers :
    print(ans)
    


    
