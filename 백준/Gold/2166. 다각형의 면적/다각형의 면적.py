import sys

n = int(sys.stdin.readline())

cordinates = []
for _ in range (n) :
    x,y = map(int,sys.stdin.readline().split())
    cordinates.append((x,y))


ans= 0

for i in range (n) :
    x1,y1 = cordinates[i]
    x2,y2 = cordinates[(i+1)%n]
    ans +=  (x1 *y2) - (x2*y1)

ans = ans * 0.5

print(abs(round(ans,1)))