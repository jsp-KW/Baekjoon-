import sys

def find(n) : 
        
    fibo=[1,2]

    for i in range(1,45):
        fibo.append(fibo[i-1]+ fibo[i])

    selected =[] 
    idx = len(fibo) -1
    sum =0

    while sum !=n:
        while sum + fibo[idx] >n :
            idx = idx-1
        sum += fibo[idx]
        selected.append(fibo[idx])
    return selected[::-1]


n = int (sys.stdin.readline().rstrip('\n'))

input =[]
for _ in range(n):
    case = int(sys.stdin.readline().rstrip('\n'))
    input.append(case)

for i in input:
    result = find(i)
    print(*result)
