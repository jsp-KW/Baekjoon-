# 맨헤튼 거리 
# abs(r1-r2) + abs(c1-c2) => 2 이하 인 경우 규칙 어김
# 대기실 5개, 각 대기실 사이즈 5x5
# 응시자 파티션 응시자 -> 맨헤튼 거리 이하여도 ㄱㅊ
# 각 대기실별 return answer길이 5, 한명이라도 규칙 x인 경우 그 대기실 0, 다 지키고 있는 대기실 1


# p : 응시자 , O : 빈테이블, X : 파티션



def solution(places):
    answer = []
    
     
    for place in places :
        is_valid = 1
        for i in range (0,5) :
            for j in range(0,5) :
                
                if place[i][j] == 'P':
                    
                    # 1. 맨해튼 거리 1일때
                    for dx,dy in  [(-1,0),(1,0),(0,-1),(0,1)] :
                        ni,nj = i+dx, j+dy
                        
                        if 0<=ni<5 and 0<=nj<5 :
                            if place[ni][nj] =='P' :
                                is_valid = 0
                                break
                                
                 # 2. 맨해튼 거리 2일때 -> 1. 두칸 (직선), 대각선
                    for dx,dy in [(-2,0),(2,0),(0,-2),(0,2)] :
                        ni,nj = i+dx, j+dy
                        mid_i, mid_j = i+dx//2 , j+dy//2
                        
                        if 0<=ni<5 and 0<=nj<5 :
                            if place[ni][nj] =='P' and place[mid_i][mid_j] !='X':
                                is_valid = 0
                                break 
                                
                    for dx,dy in [(1,1),(-1,-1),(-1,1),(1,-1)] : #대각선
                        ni,nj = i+dx, j+dy
                    
                        if 0<=ni<5 and 0<=nj<5 :
                            if place[ni][nj] == 'P' :
                                if place[i][nj] !='X' or place[ni][j] !='X':
                                    is_valid = 0
                                    break 
                    if is_valid == 0 :
                        break
                if is_valid == 0 :
                    break
                    
                
        answer.append(is_valid)


    return answer