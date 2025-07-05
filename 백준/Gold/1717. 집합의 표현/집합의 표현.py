#union find 트리 문제
import sys
N,M = map(int,sys.stdin.readline().split()) 
parent =  [i for i in range(N+1)] # 배열 초기화

def find(x) : # 밑과 같은 재귀호출로 짤 경우 메모리 초과 이슈 터짐
    # if parent[x] != x: # 위에 연결된 부모 노드가 존재하면
    #     parent[x] =  find(parent[x]) # 6 4 3 2 면 바로 2로 압축시키는 
    # return parent[x]

    # 비재귀적 방식으로 변환해서 풀어야함
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

# 큰 값의 부모가 작은 값이 되도록 
def union(a,b):
    get_a = find(a)
    get_b = find(b)

    if get_a < get_b :
        parent[get_b] = get_a
    else :
        parent[get_a] = get_b


for _ in range(M): # _식으로 사용하는것도 익숙해지기
    operation, a,b =  map(int, sys.stdin.readline().split())
    if operation ==0 :
        union(a,b)
    else :
        print("YES" if find(a) == find(b) else "NO")
