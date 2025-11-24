import sys
from collections import Counter

g,s = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().rstrip()#  찾고싶은 문자열
S = sys.stdin.readline().rstrip() # 전체 문자열

W_arr = [0] *128
S_arr = [0] *128

for ch in W :
    W_arr[ord(ch)] +=1


for ch in S[:g] :
    S_arr[ord(ch)] +=1


answer = 0

if W_arr == S_arr :
    answer +=1


for i in range (g,s) :
    S_arr[ord(S[i])] +=1
    S_arr[ord(S[i-g])] -=1

    if S_arr == W_arr :
        answer +=1

print (answer)
