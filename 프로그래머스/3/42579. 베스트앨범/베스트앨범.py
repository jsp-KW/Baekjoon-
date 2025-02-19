def solution(genres, plays):
    answer = []
    
    get_max_genres = {}
    
    for i in range (len(genres)):
        
        if genres[i] not in get_max_genres:
            get_max_genres[genres[i]] =plays[i]
        else :
            get_max_genres[genres[i]] +=plays[i]
    
    max_key = max(get_max_genres, key=get_max_genres.get)
    
    
    song_table = {}

    for i in range(len(genres)):
        if genres[i] not in song_table:
            song_table[genres[i]] = []  
        song_table[genres[i]].append((i,plays[i])) 

    for genre in song_table:
        song_table[genre].sort(key=lambda x: (-x[1], x[0])) 
    
    sorted_genres = sorted(get_max_genres.items(), key=lambda x: x[1], reverse=True)

    print ("song_table", song_table)
    print ("sorted_genres", sorted_genres)

    for gen, _ in sorted_genres:
        for idx, _ in song_table[gen][:2]:
            if idx not in answer :
                answer.append(idx)
        
    return answer

