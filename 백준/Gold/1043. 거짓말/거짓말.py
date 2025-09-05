import sys

from collections import deque
N, M = map(int, sys.stdin.readline().split())

# 진실을 아는 사람수 , 번호
# 사람수 만큼 번호가 주어짐. 번호는 1~N까지
# 3째줄 부터 , M개의 파티마다 오는 사람의 수와 번호

knowing_real = list(map(int,sys.stdin.readline().split()))
K = knowing_real[0]
truth_people = knowing_real[1:]

partys = []


for _ in range (M) :
    participant = list(map(int,sys.stdin.readline().split()))    
    partys.append(participant[1:])


if K == 0 : # 진실 아는사람x -> 최대는 파티갯수
    print (M)
else: # 아는사람이 존재하긴 하면, 
   visited = set (truth_people) # 눈을 뜬 자들..
   q = deque(truth_people) #  눈을 뜬 자들을 넣어주고,
   
   
   person_to_party = [[] for _ in range (N+1)] # 이 사람이 어디 파티에 속해있는지 

   for i, party in enumerate(partys) :
       for p in party:
           person_to_party[p].append(i)


   while q : # 큐에서 꺼내오고,
       person = q.popleft()
       for party_idx in person_to_party[person] : # 진실을 아는 자가 어디 파티에 있을지 -> 그 파티 잇는 사람들도 진실을 알게됨
           for p in partys[party_idx] : # 해당 파티의 사람들도 진실을 알게됨...
               if p not in visited : # 눈을 뜬 자들 visited 체크, q에 다시 넣기 -> 구라를 전파하러
                   visited.add(p)
                   q.append(p)

   answer = 0
   for party in partys : #  구라가 가능한 집단 확인
       can_lie = True
       for p in party : # 파티하나
           if p in visited : # 파티속 사람이 구라를 아는 사람이 발견되면, 바로 구라 x
               can_lie = False
               break
       if can_lie : #없으면 구라가능한 파티 +1
           answer+=1

   print(answer)
  
            
           
       
    
