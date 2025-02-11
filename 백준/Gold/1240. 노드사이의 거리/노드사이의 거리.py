import sys
input = sys.stdin.readline

N, M = map (int,input().split())

link_information = [[] for _ in range (N+1)]

for _ in range(N-1):
    node1,node2, distance =map(int, input().split())

    link_information[node1].append((node2,distance))
    link_information[node2].append((node1,distance))
    


def dfs(current,target,current_distance, visited) :
    if current ==target :
        return current_distance
    
    visited[current] = True

    for neighbor, neighbor_distance in link_information[current]:
        if not visited[neighbor] :
            result =dfs (neighbor,target,current_distance+neighbor_distance,visited)
            if result != -1:
                return result
    
    return -1

for _ in range(M):
    target_n1, target_n2 = map(int, input().split())

    visited = [False]*(N+1)

    res = dfs(target_n1,target_n2,0,visited)

    print(res)
    


