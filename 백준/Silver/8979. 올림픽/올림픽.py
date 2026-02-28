import sys

# 순위
# 금메달 수 더 많은
# 같으면 은메달
# 같으면 동메달

# 국가 1~N , 등수 : 더 잘한 나라의 수 +1
# 금,은,동 다 같으면 두나라의 등수는 같음

# 등수 마지막 == 국가 수

N , K = map(int,sys.stdin.readline().split())

total = []
for _ in range (N) :
    nation_num, gold, silver, bronze = map(int,sys.stdin.readline().split())
    total.append((nation_num, gold, silver, bronze))

total.sort (key = lambda x: (-x[1],-x[2],-x[3]))

rank =  1

prev_gold = total[0][1]
prev_silver =total[0][2]
prev_bronze =  total[0][3]

ranking = [(1,total[0][0]),]
for i in range (1,N) :
    target_gold, target_silver, target_broze =  total[i][1],total[i][2], total[i][3]

    if target_gold == prev_gold  and target_silver == prev_silver and target_broze == prev_bronze :
        ranking.append ((rank,total[i][0]))
        rank+=1
    else :
        rank+=1
        ranking.append((rank,total[i][0]))
    
    prev_gold = target_gold
    prev_silver = target_silver
    prev_bronze = target_broze


for t in ranking :
    if t[1] == K :
        print(t[0])
        break