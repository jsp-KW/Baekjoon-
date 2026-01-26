from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 트럭 bridge_lenth만큼 올라갈수잇고
    # 다리는 weight 이하까지 가능
    
    # 다리길이 ->  한대당 걸리는 시간,
    
    bridge = deque ([0]*(bridge_length))# 큐로 놓기
    waiting = deque (truck_weights)
    
    cur_weight = 0
    time = 0
    
    while bridge :
        time +=1 
        out_truck = bridge.popleft()
        cur_weight = cur_weight - out_truck
        
        if waiting :

            if cur_weight + waiting[0] <= weight:
                cur_truck=waiting.popleft()
                cur_weight += cur_truck
                bridge.append(cur_truck)
                
            else : bridge.append(0)
            
        else: bridge.append(0)
            
        if not waiting and cur_weight == 0 :
            return time
            break
        

        
    
  