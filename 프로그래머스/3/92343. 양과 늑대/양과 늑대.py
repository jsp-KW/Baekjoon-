def solution(info, edges):
    answer = 0
    
#     n = len(info)
    
#     tree = [[]*(n) for _ in range (n)]
#     for e in edges :
#         start,end = e
#         tree[start].append(end)

#     def dfs(sheep, wolf,candidates):
#         nonlocal answer
#         answer= max(answer, sheep)

#         for nxt in candidates:
#             next_sheep=sheep
#             next_wolf =wolf
        
#             if info[nxt] == 0 :
#                 next_sheep +=1
            
#             if info[nxt] ==1 :
#                 next_wolf +=1
                    
#             if next_sheep <= next_wolf :
#                 continue
                
#             next_candidates = candidates.copy()
#             next_candidates.remove(nxt)
#             next_candidates.extend(tree[nxt])
#             dfs(next_sheep, next_wolf, next_candidates)
    
#     dfs(1, 0, tree[0])
    
#     return answer
            
    n = len(info)
    tree = [[] *(n) for _ in range (n)]
    
    for e in edges :
        a = e[0]
        b = e[1]
        tree[a].append(b)
        
    def dfs (sheep, wolf, candidates) :
        nonlocal answer
        answer = max(answer, sheep)

        for nxt_node in candidates:

            next_sheep = sheep
            next_wolf = wolf
        
            
            if info[nxt_node] == 0 :
                next_sheep+=1
            
            if info[nxt_node] == 1:
                next_wolf +=1
            
            if next_sheep <= next_wolf :
                continue
            
            next_candidates = candidates.copy()
            next_candidates.remove(nxt_node)
            next_candidates.extend(tree[nxt_node])
            dfs(next_sheep, next_wolf, next_candidates)
    
            
            
        
        
    dfs(1,0, tree[0])    
    
        
    return answer

        
        