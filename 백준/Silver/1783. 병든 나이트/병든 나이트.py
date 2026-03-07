import sys

N,M = map(int,sys.stdin.readline().split())

# NXM

def SOLVE (n, m) :

    if n == 1 :
        return 1
    
    if n ==2 : # 높이가 2라면,
        return min (4, (m+1) //2)
    
    else :# 4가지 다 쓰면, 가로 6칸 필요 출발지점 1열이니, 1+6 해서 7열까지, 즉, 6열보다 작거나 같은 경우는, 4개 방문이 최대
        if m<= 6 :
            return min(m,4)
        elif m>=7 : # 7보다 큰 경우에는, 4가지 방법을 다쓰고, 그다음 아무런 제약사항이 없어서 최대 M-2 칸 방문가능
            return m-2



print(SOLVE(N,M))