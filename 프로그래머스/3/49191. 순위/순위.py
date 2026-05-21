def solution(n, results):
#     answer = 0
#     winners =[set() for _ in range(n+1)]
#     losers =[set() for _ in range(n+1)]
    
#     for res in results:
#         win, lose= res
#         winners[win].add(lose)
#         losers[lose].add(win)
    
#     print ("winners ", winners)
#     print ("losers", losers)
#     for cur_player in range (1, n+1): 
#         #현재 플레이어가 이긴애들에게 현재플레이어를 이겨버린 승자 업데이트
#         for lose_player in  (winners[cur_player]):
#             losers[lose_player].update(losers[cur_player])
#         for win_player in (losers[cur_player]):
#             winners[win_player].update(winners[cur_player])
            
#     for i in range(1,n+1):
#         if len(winners[i]) +len(losers[i]) == n-1:
#             answer+=1
            
    answer = 0
    win_set = [set () for _ in range (0,n+1)]
    lose_set = [set() for _ in range (0,n+1)]
    
    for res in results :
        winner, loser = res
        win_set[winner].add (loser)
        lose_set[loser].add (winner)
    
    
    for i in range (1, n+1) : # 1->2 , 2->3
        current_player =i
        for losed_by_cur in win_set[current_player] : # 1번이 이긴 사람들 : 2,3이라면,
            lose_set[losed_by_cur].update (lose_set[current_player])
        for win_cur in lose_set[current_player] : # 5->1->2
            win_set[win_cur].update (win_set[current_player])
            
            
    for i in range(1,n+1) :
        if len(win_set[i]) + len(lose_set[i]) == n-1 :
            answer+=1
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    return answer