# 입력 1. 크레인 N 개수 (50 보다 작거나 같은 자연수)
# 입력 2. 각 크레인의 무게 제한 ( <= 10000) 
# 입력 3. 박스의 수 ( <= 10000)
# 입력 4. 박스의 무게  (<=1000000)

# 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하라
# 만약 모든 박스를 배로 옮길 수 없으면  -1 을 출력한다.
import sys

N = int(sys.stdin.readline().rstrip())
crain_weight= list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
box_weight = list(map(int, sys.stdin.readline().split()))


# N개가 크레인이니까 N 개의 묶음으로 box들의 무게 리스트를 순회해서
# 만약 크레인이 들수있는 무게제한 리스트에서 무게제한을 만족한다면 그 부분을 박스 무게리스트에서 제거
# 1,2 ~ N-1 대를 썻더라도 똑같이 1분 추가시간 쓴걸로 처리
# 무게 제한 리스트에 숫자가 없어지면 처리완료 이후 걸린 시간 출력

crain_weight.sort(reverse=True)
box_weight.sort(reverse=True)

if box_weight[0] > crain_weight[0] :
    print(-1)
    sys.exit()

time = 0

while box_weight :
    crain_idx = 0
    box_idx =0


    while crain_idx < N and box_idx < len(box_weight) :
        if crain_weight[crain_idx] >= box_weight [box_idx] :
            box_weight.pop(box_idx)
            crain_idx +=1
        else:
            box_idx = box_idx +1


    time = time+1

print(time)
