import heapq
# 최소비용정리,

def solution(n, costs):
    # n : 섬의 개수 
    graph = [[] for _ in range(n) ]
    for cost in costs :
        island1, island2, c = cost 
        graph [island1].append ((c,island2))
        graph [island2].append ((c,island1))
    
    
    # 다익스트라
    # 모든섬 통행 -> 최소비용
    def prim (start) :
        visited = [False] *(n)
        cnt = 0
        total_cost = 0
        q = [(0,start)]
        
        while q :
            cur_cost, cur_node = heapq.heappop(q) 
            if visited[cur_node]  : #방문한 곳이라면? 스킵
                continue
            visited[cur_node] = True
            total_cost = total_cost + cur_cost
            cnt +=1
            if cnt == n :
                return total_cost
            for nxt_cost, nxt_node in graph [cur_node] :
                if not visited[nxt_node] :
                    heapq.heappush (q,(nxt_cost,nxt_node))
            
            
    
        
    return prim(0)