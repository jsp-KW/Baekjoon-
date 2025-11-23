
# 가로 * 세로 =  brown + yellow
# w, h 의 순서쌍 을 구하고,  w가 h보다 큰 걸 구한다.
# yellow 가로 +2 -> 전체 가로 , yellow  세로+2 ->  전체 세로
# brown = 2w+2h+4

def solution(brown, yellow):
    for height in range (1, yellow+1) :
        if yellow % height ==0 :
            width = yellow // height
    
        if 2*width + 2*height +4 == brown :
            return [width+2,height+2]
  



