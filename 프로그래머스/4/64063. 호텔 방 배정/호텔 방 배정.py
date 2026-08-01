def solution(k, room_number):
 
    
    # 총 방 k개
    # 1~K 번호로 구분
    
    
    # 신청한 순서 --> 방번호 제출 --> 비어있으면 즉시 배정, 배정되어있다면 원하는 방보다 번호 크고 비어있는 방 선택--> 가장 작은 번호 배정
    
    
    # 각 고객에게 배정되는 방번호를 순서대로 배열에 담기
    
    # room_number : 고객들이 원하는 방 번호 
    # result : 고객에게 배정되는 방번호
    

    answer = []
    
    # 효율성 떵인 직관적인거
#     room_used = set()
    
#     for r in room_number :
#         while r in room_used:
#             r+=1
        
#         room_used.add(r)
#         answer.append(r)


    next_room=  {}
    
    def find(room) :
        path = []
        
        while room in next_room :
            path.append(room)
            room= next_room[room]
            
        for visited in path :
            next_room[visited] = room
        
        return room
    
    for room in room_number :
        result = find(room) 
        answer.append(result)
        next_room[result] = find(result+1)
        
    return answer