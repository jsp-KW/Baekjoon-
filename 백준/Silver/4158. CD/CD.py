import sys
answers =[]
while True :
    N,M = map(int,sys.stdin.readline().split())
    
    if N == 0 and M ==0 :
        break
    sang = []
    sun=  []
    for _ in range (N) :
        sang_cd_num = int(sys.stdin.readline())
        sang.append(sang_cd_num)

    for _ in range (M) :
        sun_cd_num = int(sys.stdin.readline())
        sun.append(sun_cd_num)

    A=  set(sang)
    B= set(sun)

    answers.append(len(A&B))

for ans in answers:
    print(ans)