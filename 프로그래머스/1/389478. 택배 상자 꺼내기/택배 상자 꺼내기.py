def solution(n, w, num):
    answer = 0
    
    
    # 택배 상자 개수 n
    # 가로로 놓는 상자 개수 w
    # 꺼내려는 번호 num
    
    # 꺼내는 상자 포함해서 몇개를 꺼내야하는지 return
    
    
    # w개 만큼 가로로 놓는다
    
    if n % w == 0 :
        row  = n //w
    else :
        row = n//w +1
    
    col = w
    
    origin_num = row * col
    arr = [[0] * (col) for _ in range (row)]
    
    # n부터 채워서
    cnt = origin_num - n
    
    top_layer = row
    if top_layer % 2==0 :
        for i in range (cnt) :
            arr[0][i] = -1
    else : #col-1부터 
        for i in range (cnt):
            arr[0][col-1-i] = -1
  
    for r in range (row) : #0,1,2,3
        layer = row -r 
        if layer % 2 ==0 :
            for c in range (col) :
                if arr[r][c] == 0 :
                    arr[r][c] = n
                    n= n-1
        else :
            for c in range (col-1, -1, -1) :
                if arr[r][c] == 0 :
                    arr[r][c] = n
                    n= n-1
    

    for a in arr:
        print (a)
    target_row, target_col = 0,0
    for i in range (row) :
        for j in range (col) :
            if arr[i][j] == num :
                target_row = i
                target_col = j
             
                
    for i in range (target_row+1) :
        if arr[i][target_col] >0 :
            answer+=1
                
                
    
                
    return answer