import sys

def find(n) : 
        
    fibo=[1,2] #피보나치를 이용하기 위하여.0,1,1,2,3,5, .... 1134903170

    for i in range(1,45):
        fibo.append(fibo[i-1]+ fibo[i])

    selected =[] 
    idx = len(fibo) -1
    sum =0

    while sum !=n: # 주어진 수를 맞춰야하므로
        while sum + fibo[idx] >n : # 조건에 맞는 값이 제일 뒤에서 최대값이므로
            idx = idx-1 # 조건을 찾을때까지 뒤에서 찾는다
        sum += fibo[idx]
        selected.append(fibo[idx])
    return selected[::-1] # 리스트를 뒤집어서 반환한다. 오름차순으로 출력하기 위해서


n = int (sys.stdin.readline().rstrip('\n'))

input =[]
for _ in range(n):
    case = int(sys.stdin.readline().rstrip('\n'))
    input.append(case)

for i in input:
    result = find(i)
    print(*result)# *을 이용해서 값1 값2 값3 의 형태로 출력한다.
