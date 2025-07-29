import sys

X,Y = map(int, sys.stdin.readline().split())

Z = int(Y*100/X)


if Z >= 99 :
    print (-1)
    exit()


left = 1
right = 1000000000
answer = -1

while left <= right :
    mid = (left+right) //2
    newZ = int((Y +mid) *100 /(X+mid))

    if newZ > Z:
        answer = mid
        right = mid -1
    else :
        left = mid +1

print (answer)
