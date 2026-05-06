def solution(numbers, hand):
    answer = ''
    
    #2,5,8,0 일때는 현재 두 엄지손가락의 위치에서 더 가까운 엄지손가락을 사용한다
    #
    
    cur_left_y, cur_left_x =3,0
    cur_right_y, cur_right_x = 3,2
    
    
    # [1,2,3]
    # [4,5,6]
    # [7,8,9]
    # [*,0,#]

    
    for num in numbers:         
        if num in [1,4,7] :
            answer += 'L'
            
            if num == 1 :
                cur_left_y, cur_left_x = 0 ,0
            elif num ==4 :
                cur_left_y, cur_left_x = 1,0
            elif num== 7 :
                cur_left_y, cur_left_x = 2,0
                
        
        elif num in [3,6,9]: 
            answer += 'R'
            
            if num ==3 :
                cur_right_y,cur_right_x = 0,2
            elif num == 6 :
                cur_right_y , cur_right_x =1,2
            elif num == 9 :
                cur_right_y, cur_right_x = 2,2
        else :
            # 2,5,8,0 중 하나
            # [(0,1), (1,1), (2,1), (3,1)] 이란 말
            if num == 2 :
                target_y, target_x = 0,1 
            elif num == 5 :
                target_y, target_x = 1,1
            elif num == 8 :
                target_y, target_x = 2,1
            else :
                target_y, target_x = 3,1 
            
            
            left_distance =abs (cur_left_y -target_y)  + abs ( cur_left_x - target_x)
            right_distance = abs (cur_right_y - target_y) + abs ( cur_right_x - target_x)
            
            if left_distance == right_distance  :
                if hand =='left' :
                    answer +='L'
                    cur_left_y, cur_left_x =  target_y, target_x
                else :
                    answer +='R' 
                    cur_right_y, cur_right_x = target_y, target_x
                    
            elif left_distance < right_distance :
                answer +='L'
                cur_left_y, cur_left_x =  target_y, target_x
              
            else:
                answer +='R'
                cur_right_y, cur_right_x = target_y, target_x
        
    
    return answer