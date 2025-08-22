import sys

N, new_score, P = map(int, sys.stdin.readline().split())


if N == 0 :
    print(1)

if N >0 :
    scores = list(map(int,sys.stdin.readline().split()))

    if new_score <= scores[-1] and N == P :
        print(-1)
        sys.exit(0)


      
    rank = 1
    for s in scores :
        if s > new_score :
            rank +=1

    print(rank)

        

