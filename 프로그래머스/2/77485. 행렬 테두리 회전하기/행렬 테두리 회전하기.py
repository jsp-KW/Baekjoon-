def solution(rows, columns, queries):
    answer = []
    
#     maps = [[0]*(columns+1) for _ in range (rows+1)]
    
#     # 숫자 채우기
    
#     init_val = 1
#     for i in range (1,len(maps)) :
#         for j in range (1,len(maps[i])) :
#             maps[i][j] = init_val
#             init_val +=1
            
#     for q in queries :
#         x1,y1,x2,y2 = q
        
#         # x1,y1 에서 -> x1이 x2가 될때까지
#         # y1이 y2가 될때까지
        
#         # 왼쪽 , 오른쪽 아래, 오른쪽->왼쪽, 아래쪽->위쪽
        
#         temp = maps[x1][y1]
#         mn = temp
        
#         for x in range (x1,x2) :
#             maps[x][y1] = maps[x+1][y1]
#             mn = min(mn, maps[x][y1])
            
#         for y in range (y1,y2) :
#             maps[x2][y] = maps[x2][y+1]
#             mn = min(mn, maps[x2][y])
            
#         for x in range (x2,x1,-1) :
#             maps[x][y2] = maps[x-1][y2]
#             mn = min(mn, maps[x][y2])
        
#         for y in range (y2,y1+1,-1) :
#             maps[x1][y] = maps[x1][y-1]
#             mn = min(mn,maps[x1][y])
            
#         maps[x1][y1+1] = temp
#         answer.append(mn)


    maps = [[0]* (columns+1) for _ in range (rows+1)]
    num =1
    
    for i in range (1, rows+1) :
        for j in range (1, columns+1) :
            maps[i][j] = num;
            num +=1
    
    
    for q in queries :
        x1,y1,x2,y2 = q # 행 열 행 열
        
        prev = maps[x1][y1]
        min_val = prev
        
        #  y1----y2 x1 고정
        
        for y in range (y1+1, y2+1) :
            cur = maps[x1][y]
            maps[x1][y] = prev
            prev= cur
            min_val = min(min_val, cur)
            
            
        # x1-----x2  y2고정
        
        for x in range (x1+1, x2+1) :
            cur = maps[x][y2]
            maps[x][y2] = prev
            prev =cur
            min_val = min(min_val, cur)
            
        
        # y2------y1 x2고정
        for y in range (y2-1, y1-1,-1) :
            cur = maps[x2][y]
            maps[x2][y]= prev
            prev = cur
            
            min_val= min(min_val, cur)
        
        # x2----x1 y1고정
        
        for x in range (x2-1, x1-1, -1) :
            cur = maps[x][y1]
            maps[x][y1]= prev
            prev = cur
            
            min_val = min(min_val,cur)
        answer.append(min_val)
        
            
    return answer