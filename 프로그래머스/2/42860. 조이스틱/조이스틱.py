def solution(name):
    answer = 0
    # A로만 이루어져있음
    # 다음, 이전, 왼쪽(첫번째 인덱스에서 실행시 마지막 문자로) , 오른쪽(마지막 위치일때 실행시 첫 번째 커서)
    
    # 조이스틱 조작 횟수의 최소값을 RETURN 
    #name 을 어떻게 조작해야, 최소가 될까?
    
    # A B C D E / F G H I J / K L M N O / P Q R S T/ U V W X Y/ Z
    
    
    # 연속된 구간 찾기
    # NAME에서
    # 커서 좌우 / 알파벳 바꾸는거 독립적
    # 알파벳 바꾸는건 -> 무조건 드는 비용
    #
    n = len(name)
    up_down = sum(min(ord(c)-ord('A'), ord('Z')- ord(c)+1) for c in name)

    min_move = n-1
    # 고치고, 중간에 '연속된 'a'를 만나면, 유턴해서 고칠곳 까지 가기 vs 유턴하지 않고 연속 a 를 뚫고 가서 고치기
    # B A C C 라면, 
    # B 고치고, A 햇을때
    for i in range (n) : 
        next_idx =  i+1
        while next_idx < n and name[next_idx] =='A' :
            next_idx +=1
            
        dist1 = i+i + (n-next_idx)
        dist2 = (n-next_idx) + (n- next_idx) + i
        
        min_move = min(min_move, dist1, dist2)
        
    return up_down + min_move

             