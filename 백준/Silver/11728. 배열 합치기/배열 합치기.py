import sys

N,M = map(int,sys.stdin.readline().split())
A = list (map (int, sys.stdin.readline().split()))
B = list (map(int,sys.stdin.readline().split()))

# 두 배열을 합친다음 정렬해서 출력
# 두배열은 이미 정렬 되어있음

i = j = 0 

res = []

while i <N and j <M :
    if A[i] < B[j] :
        res.append(A[i])
        i +=1
    else :
        res.append(B[j])
        j+=1

if i <N :
    res.extend (A[i:])
if j <M :
    res.extend(B[j:])

print (*res)