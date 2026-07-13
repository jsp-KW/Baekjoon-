from collections import deque

def solution(begin, target, words):
#     answer = 0
#     visited= [False]*(len(words))
#     if target in words:
#         q= deque([(begin,0)])
        
#         while q:
#             cur_word, step = q.popleft()
            
#             if cur_word == target:
#                 return step
            
#             for i in range(0,len(words)):
#                 if not visited[i] :
#                     differ_cnt =0
#                     for j in range(0,len(words[i])):
#                         if cur_word[j]!= words[i][j]:
#                             differ_cnt+=1
                            
                    
#                     if differ_cnt==1:
#                         visited[i]= True
#                         q.append((words[i],step+1))    
#                     else: continue
    
    #else: return 0
    answer = 0
    #한번에 한개의 알파벳,
    #words에 있는 단어로만 변환 가능
    n = len(words)
    visited = [False] *(n)
    if target not in words :
        return 0
    else:
        q= deque ([(begin, 0)])
        while q :
            cur_word, step = q.popleft()
            if cur_word == target :
                return step
            
            for i in range (0, len(words)) :
                if visited[i] :
                    continue
                    
                next_word = words[i]
                diff = 0
                for j in range (0, len(cur_word)):
                    if next_word[j] != cur_word[j] :
                        diff +=1
                
                if diff >1 :
                    continue
                else:
                    visited[i] = True
                    q.append((next_word, step+1))
    
    
                
            