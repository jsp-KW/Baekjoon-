import heapq

def solution(jobs):
    answer = 0
    # 소요시간/요청시각/작업번호 작은것
    # 반환시간= 종료시각- 요청시각
    # 평균 반환 시간
    finish_q= []
    wait_q=[]
    ready_q= []
    for i in range(0,len (jobs)):
        task,ask_time, take_time= i+1, jobs[i][0],jobs[i][1]
        heapq.heappush(wait_q,(ask_time,take_time,task )) # /요청/소요/작업
    
    t= 0

    while wait_q or ready_q:
            
        #시간t를 기준으로, 대기큐에서 준비큐로 갈 친구 탐색
        while wait_q and wait_q[0][0] <= t :
            ask_time,take_time,task =(heapq.heappop(wait_q))
            heapq.heappush(ready_q, (take_time, ask_time, task))
        
        if ready_q:
            target_process = heapq.heappop(ready_q)
            t = t+ target_process[0]
            finish_q.append (t - target_process[1])
        else :
            t= wait_q[0][0]
    
    return sum(finish_q) // len(jobs)