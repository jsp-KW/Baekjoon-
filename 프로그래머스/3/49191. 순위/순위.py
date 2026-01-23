def solution(n, results):
    answer = 0
    winners = [set() for _ in range (n+1)]
    losers = [set() for _ in range (n+1)]

    for res in results :
        win_player, lose_player = res
        winners [win_player].add(lose_player)
        losers [lose_player].add(win_player)
        
    for i in range (1, n+1) :
        for win_i in losers[i]:# i가 이긴 사람들
            winners[win_i].update (winners[i])
        for lose_i in winners[i] :
            losers[lose_i].update (losers[i])
    
    for i in range (1, n+1) :
        if len(winners[i]) + len(losers[i]) == n-1:
            answer+=1
            
    
    return answer