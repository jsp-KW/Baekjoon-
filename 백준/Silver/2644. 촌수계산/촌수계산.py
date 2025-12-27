import sys
from collections import deque


# visited 배열을 거리배열로 쓰기
# 양방향 관계, bfs 로직순회
# 좌표 bfs 문제랑 살짝 다른 풀이 이해
n = int (sys.stdin.readline()) # 전체 사람 수
target1, target2 = map (int,sys.stdin.readline().split()) #  서로 다른 두사람의 번호
m =  int (sys.stdin.readline()) # 관계의 개수

pepoles = [[] for _ in range (n+1)]
for _ in range (m) :
    parent_num, person_num  = map (int,sys.stdin.readline().split())
    pepoles[person_num].append(parent_num)
    pepoles[parent_num].append (person_num)

visited = [-1] * (n+1) 

def bfs (start) :
    idx = start 
    
    visited[idx] = 0 
    q = deque([idx])

    while q :
        cur_idx = q.popleft()

        for next in pepoles[cur_idx] :
            if  visited[next]  == -1: 
                visited[next]  = visited[cur_idx] + 1
                q.append(next)
    
    return visited[target2]


print (bfs(target1))

