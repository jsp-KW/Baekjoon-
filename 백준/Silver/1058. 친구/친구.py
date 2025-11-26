import sys
from collections import deque

N = int(sys.stdin.readline())

# A가 또 다른 사람 B의 2-친구가 되기 위해선, 두사람이 친구 OR A와 친구, B와 친구인 C의 사람이 존재해야함
# A B 친구면, B A 도 친구이도 A와 A는 친구가 아니다.
# 가장 유명한 사람의 2-친구의 수를 출력하자
# 거래가 2 이하 즉, 1,2 인 걸로 제한
# 직접적인 친구 + 통해서 아는 친구 
# 그래프임, 격자 x


# 그래프임을 인식
# 길이를 배열로해서 
def bfs (start) :
    
    visited= [False] * N
    dist = [0] * N
    
    visited[start] = True
    q = deque()
    q.append(start)

    while q  :
        cur= q.popleft()
        
        for next in range (N) :
            if friend_maps[cur][next] == 'Y' and not visited[next]:
                dist[next]= dist[cur] +1

                if dist[next] <=2:
                    visited[next] = True
                    q.append(next)

    # 2이하인 dist 카운트 
    
    result = 0

    for i in range(N):
        if 1<= dist[i] <=2:
            result +=1

    return result


friend_maps = []

for _ in range (N) :
    temp = list(map(str,sys.stdin.readline().rstrip()))
    friend_maps.append(temp)

answer = 0
for i in range (N) :
    answer= max(answer, bfs(i))

print (answer)

    