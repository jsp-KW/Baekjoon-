import sys

N,M = map(int, sys.stdin.readline().split())

girl_group = dict()

for _ in range(N) :
    group_name = sys.stdin.readline().strip()
    inner_loop_cnt = int(sys.stdin.readline().strip())

    girl_group[group_name] = []
    for _ in range(inner_loop_cnt):
        
        member = sys.stdin.readline().strip()
  
        girl_group[group_name].append(member)


answer = []       

for _ in range(M) :
    mem_or_group = sys.stdin.readline().strip()
    type_of_quize = int(sys.stdin.readline().strip())

    if type_of_quize ==1 : #해당 멤버가 속한 팀의 이름을 출력
        for group_name, members in girl_group.items() :
            if mem_or_group in members :
                answer.append(group_name)
                break
    elif type_of_quize ==0 : # 해당 멤버가 속한 그룹의 모든 멤버 출력
        for members in sorted(girl_group[mem_or_group]) :
            answer.append(members)

for ans in answer :
    print (ans)