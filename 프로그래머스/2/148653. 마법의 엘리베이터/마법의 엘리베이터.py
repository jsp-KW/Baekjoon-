from collections import deque

def solution(storey):
    answer = 0
    # 현재층과 버튼 값 더한 결과가 <0 이면 엘레베이터는 움직이지 않음
    # 0층이 가장 아래층, 엘레베이터는 현재 민수가 있는 층
    # 돌의 최소 개수를 구하자
    
#     arr = [0]*(storey+1)
#     distance = [-1] *(storey+1)
    
#     move =[]
    
#     length = len(str(storey))
#     # 1000 000 000
#     # 1000 000 00
#     # 1000 000 0
#     # 1000 000 
#     # 1000 00
#     # 1000 0
#     # 1000
#     # 100
#     # 10
#     # 1
#     length =length -1
#     while length >=0 :
#         temp= "1"
#         move .append (int((temp + "0"*length)))
#         move.append (-int((temp+ "0" *length)))
#         length -=1

#     def bfs (start) :
#         distance[start] = 0
#         q = deque([start])
        
#         while q :
#             cur= q.popleft()
            
#             if cur == 0 :
#                 return distance[0]
#             for num in move :
#                 nxt = cur +num 
#                 if nxt <0 :
#                     continue 
#                 if 0<= nxt <= storey and distance[nxt] ==-1 :
#                     distance[nxt] = distance[cur] +1
#                     q.append(nxt)
    
    
#     answer = bfs(storey)   

    # 6,7,8,9 인 경우 한칸 올라가서 내려오는게 더 이득
    # 1,2,3,4 인 경우 한칸씩 내려갔다가 올라오는게 더 이득
    # 5는 다음 숫자를 보고 판단
    # 255인 경우
    while storey > 0 :
        digit = storey % 10
        next_digit = (storey //10) % 10
        
        if digit <5 :
            answer += digit 
            storey = storey // 10
            continue 
        elif digit >5 :
            answer += 10 - digit 
            storey = storey // 10 +1 
            continue 
        
        else :
            answer +=5 
            
            if next_digit >=5 :
                storey = storey // 10 +1

            else :
                storey = storey // 10
                
            
    return answer