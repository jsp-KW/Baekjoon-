from math import ceil

def solution(players, m, k):
    answer = 0
    timer = []
    
    for t in range(24) :
        timer = [time-1 for time in timer]
        
        timer = [time for time in timer if time > 0]
        
        required = players[t] // m
        
        if players[t] >= (len(timer) +1) * m:
            to_add = required - len(timer)
            answer += to_add
            
            
            for _ in range(to_add) :
                timer.append(k)
            
            
    return answer