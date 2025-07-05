import sys
N = int(sys.stdin.readline())

buildings = []
for i in range (0,N):
    buildings.append(list(map(int, sys.stdin.readline().split())))

temp = []
answer = 0
for li in buildings :
      
    if len(temp) ==0 and li[1]!= 0: # stack 이 비어있고 높이가 0이 아니면 첫 건물
        temp.append(li[1])
        answer += 1
    
    else: # 스택이 비어있지 않고
        while temp and  temp[-1] > li[1]: # 새 건물의 높이가 이전 건물보다 낮은 경우
            temp.pop() # 새 건물 높이보다 큰 건물 높이 모두 제거

        if li[1] !=0 and(not temp or temp[-1] < li[1] ): #0 이 아니면서 새건물높이가 더 크거나 스택에 높이가 없는 경우
            temp.append(li[1])
            answer +=1
        
print (answer)