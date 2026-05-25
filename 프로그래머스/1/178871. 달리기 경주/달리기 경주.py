def solution(players, callings):
    answer = []
    
    # mumu soe kai poe mine
    # mumu kai soe poe mine
    # mumu kai soe mine poe
    # mumu kai mine soe poe
    
    # for player in callings :
    #     cur = player
    #     for i in range (0, len(players)) :
    #         if players[i] == cur :
    #             temp = players[i-1]
    #             players[i-1] = cur
    #             players[i] = temp
    #             break
                
    cur_pos = {}
    
    for i in range (0, len(players)) :
        cur_pos[players[i]] = i
    
    for call_player in callings :
        cur_idx = cur_pos [call_player]        
        prev_idx = cur_idx -1
        
        prev_player = players[prev_idx]
        
        players[prev_idx] = call_player
        players[cur_idx] = prev_player
       
        cur_pos[prev_player] = cur_idx
        cur_pos[call_player] = cur_idx -1
    return players