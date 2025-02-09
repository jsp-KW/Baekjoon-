
T = (int)(input())


        
for _ in range (T) :
    n,k,t,m = map (int, input().strip().split())
    # 여기다가 점수 저장할 리스트를 추가해야할 거같은데
    
    score_list = [[0]* (k+1) for _ in range (n+1)] 
    submit_list = [0] *(n+1)
    submit_time_list = [0] * (n+1)
    

    for time in range (0,m):
        i,j,s = map (int, input().strip().split())
        # 팀 별 문제번호, 점수 배점 입력 받기
        score_list[i][j] =max (s, score_list[i][j])
        submit_list[i] = submit_list [i]+1
        submit_time_list[i] = time+1


    result =[]
    for i in range (1, n+1) :
        total_score = sum (score_list[i])
        result.append((total_score, submit_list[i],submit_time_list[i], i))

    result.sort (key=lambda x : (-x[0],x[1],x[2]))


    # tuple 로 저장한 점수, 제출횟수, 제출 시간
    # 을 순회해야하므로,

    rank = 1
    for tup in result :
        if tup[3] == t :
            print (rank)
            break
        rank = rank+1
        
        
        

        