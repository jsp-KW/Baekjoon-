def solution(citations):
    citations.sort()
    # 0 1 3 5 6
    for i in range (0, len(citations)) :
        temp = len(citations) - i 
        if citations[i] >= temp:
            return temp
        
    return 0