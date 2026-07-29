def solution(genres, plays):
    answer = []
    
    
    # 1. 속한 노래가 많이 재생된 장르 먼저
    # 2. 장르 내에서 많이 재생된 노래 먼저
    # 3. 장르 내에서 재생횟수 같으면 고유번호 낮은 노래 순서
    
    get_max_genres = {}
    
    for i in range (0, len(genres)) :
        if genres[i] not in get_max_genres :
            get_max_genres[genres[i]] =  plays[i]
        else:
            get_max_genres[genres[i]]  += plays[i]
    
    
    temp = list(get_max_genres.items())
    temp.sort(key= lambda x : -x[1])
    
    max_genres = temp[0][0]
    
 
    
    for genre, play in temp :
        first_cands = []

        for i in range (0,len(genres)) :
            if genres[i] == genre :
                first_cands.append((i,plays[i]))
        
        first_cands.sort(key= lambda x : (-x[1], x[0]))
        
        if len(first_cands) <2 :
            answer.append (first_cands[0][0])
        else:
            for i in range (2) :
                answer.append(first_cands[i][0])
    
    return answer

