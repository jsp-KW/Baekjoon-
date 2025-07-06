### greedy 
#   핵심 아이디어 -> 문제에 힌트가 존재함 대부분
#   반복문 사용시 거꾸로 순회하는 방향 3가지 인자 시작, 끝, -step
# ###
import sys

N,K = map(int,sys.stdin.readline().split()) # 여러개를 한줄로 입력받으니 

coins =[]
for i in range(N) :
    coin = int(sys.stdin.readline()) # 하나씩 입력받으므로

    coins.append(coin)

# K 원을 만드는데 필요한 동전 개수의 최솟값
# 값어치가 큰 동전을 많이 쓰면 개수 최소가 된다

result = 0 # 결과 저장 변수 result

for i in range (len(coins)-1, -1, -1) :
    if K != 0 : # 동전을 사용해서 K 값이 되기 전까지
        result = result + ( K //coins[i] )
        K = K % coins[i]
    else : # K값이 되면 종료
        break

print (result)