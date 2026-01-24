from collections import deque

def solution(begin, target, words):
    answer = 0
    visited= [False]*(len(words))
    if target in words:
        q= deque([(begin,0)])
        
        while q:
            cur_word, step = q.popleft()
            
            if cur_word == target:
                return step
            
            for i in range(0,len(words)):
                if not visited[i] :
                    differ_cnt =0
                    for j in range(0,len(words[i])):
                        if cur_word[j]!= words[i][j]:
                            differ_cnt+=1
                            
                    
                    if differ_cnt==1:
                        visited[i]= True
                        q.append((words[i],step+1))    
                    else: continue
    
    else: return 0
