def solution(routes):
    # 고속도로 이용하면서 단속용 카메라는 한번은 만나야함
    # 모든 차량이 한번은 단속용 카메라를 만나게 하려면, 최소 몇대의 카메라?
    # routes[i][0] 은 진입, routes[i][1] 은 나간 지점
    
    answer = 0
    # 지점x가 최대한 다른 경로들하고 많이 겹쳐야함
    # 
    
    routes.sort (key = lambda x : (x[1]))
    camera_loc = -30001
    
    for r in routes :
        if r[0] <= camera_loc  and camera_loc <= r[1] :
            continue
        else :
            answer+=1
            camera_loc = r[1]
            
    
    return answer