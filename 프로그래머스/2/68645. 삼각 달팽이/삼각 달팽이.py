def solution(n):
  
    i =1

    arr = []
    
    for i in range (1,n+1):
        temp = [0]* (i)
        arr.append(temp)
    
    dr = [1, 0 , -1]
    dc = [0,1,-1]
    
    num =1
    row =-1
    col = 0
    direction = 0
    
    for length in range(n, 0,-1):
        for _ in range (length):
            row += dr[direction]
            col+= dc[direction]
            
            arr[row][col] = num
            num +=1
            
            
        direction = (direction +1)%3
    answer = []
    for a in arr :
        for ans in a :
            answer.append(ans)
    return answer