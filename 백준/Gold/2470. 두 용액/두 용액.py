import sys
N = int(sys.stdin.readline())

min = 0

li = list(map(int, sys.stdin.readline().split()))  
li.sort()

left,right = 0, N-1

closet_sum = float('inf')
ans = (0,0)
while left < right :
    total = li[left] + li[right]

    if abs(total) < closet_sum :
        closet_sum = abs(total)
        ans = (li[left], li[right])

    if total <0 :
        left +=1
    else :
        right-=1

print(ans[0],ans[1])