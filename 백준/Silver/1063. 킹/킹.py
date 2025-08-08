import sys

#R,L,B,T 오른쪽 한칸, 왼쪽한칸, 아래로 한칸, 위로 한칸
#RT,LT,RB,LB 오른쪽 위 대각선, 왼쪽위, 오른쪽아래, 왼쪽아래

king_location, rock_location, moving_count = sys.stdin.readline().strip().split()

moving_count = int(moving_count)
maps =[[0]*8 for _ in range(8)]
# 0,0이면 (8,a)
#4,4이면 (4,e)
#5,4 -> 3,e
how_to_move = []
for _ in range(moving_count) :
    m = sys.stdin.readline().strip()
    how_to_move.append(m)


y = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
     'E': 4, 'F': 5, 'G': 6, 'H': 7}


get_col_king =y[king_location[0]]
get_row_king =abs(int(king_location[1]) - 8)

get_col_rock =y[rock_location[0]]
get_row_rock =abs(int(rock_location[1]) - 8)

maps[get_row_rock][get_col_rock] = 1
maps[get_row_king][get_col_king] = 1


for move in how_to_move :
     if len(move) == 1:

        if move == 'R' and get_col_king + 1 <= 7: # 킹 위치 확인
            if get_row_king == get_row_rock and get_col_king + 1 == get_col_rock: # 킹 오른쪽으로 움직인 위치가 돌 위치랑 겹치는 경우
                if get_col_rock + 1 <= 7: # 돌 위치가 범위 안에 있을경우
                    get_col_rock += 1
                    get_col_king += 1
            else: # 겹치지 않은 경우에는 킹만 오른쪽으로 이동
                get_col_king += 1

        if move == 'L' and get_col_king - 1 >= 0:
            if get_row_king == get_row_rock and get_col_king - 1 == get_col_rock:
                if get_col_rock - 1 >= 0:
                    get_col_rock -= 1
                    get_col_king -= 1
            else:
                get_col_king -= 1

        if move == 'B' and get_row_king + 1 <= 7:
            if get_col_king == get_col_rock and get_row_king + 1 == get_row_rock:
                if get_row_rock + 1 <= 7:
                    get_row_rock += 1
                    get_row_king += 1
            else:
                get_row_king += 1

        if move == 'T' and get_row_king - 1 >= 0:
            if get_col_king == get_col_rock and get_row_king - 1 == get_row_rock:
                if get_row_rock - 1 >= 0:
                    get_row_rock -= 1
                    get_row_king -= 1
            else:
                get_row_king -= 1

     elif len(move) == 2:

        if move == 'RT' and get_col_king + 1 <= 7 and get_row_king - 1 >= 0:# 오른쪽 위 대각선으로 이동한 위치가 범위내에 있어야하고
            if get_col_king + 1 == get_col_rock and get_row_king - 1 == get_row_rock: # 오른쪽 위로 이동한 킹의 위치가 돌이랑 겹친다면
                if get_col_rock + 1 <= 7 and get_row_rock - 1 >= 0:# 돌이 일단 범위 내에 있으면, 돌과 킹 이동
                    get_col_king += 1
                    get_row_king -= 1
                    get_col_rock += 1
                    get_row_rock -= 1
            else: # 돌하고 안 겹치는 경우, 킹만 이동
                get_col_king += 1
                get_row_king -= 1

        if move == 'LT' and get_col_king - 1 >= 0 and get_row_king - 1 >= 0:
            if get_col_king - 1 == get_col_rock and get_row_king - 1 == get_row_rock:
                if get_col_rock - 1 >= 0 and get_row_rock - 1 >= 0:
                    get_col_king -= 1
                    get_row_king -= 1
                    get_col_rock -= 1
                    get_row_rock -= 1
            else:
                get_col_king -= 1
                get_row_king -= 1

        if move == 'RB' and get_col_king + 1 <= 7 and get_row_king + 1 <= 7:
            if get_col_king + 1 == get_col_rock and get_row_king + 1 == get_row_rock:
                if get_col_rock + 1 <= 7 and get_row_rock + 1 <= 7:
                    get_col_king += 1
                    get_row_king += 1
                    get_col_rock += 1
                    get_row_rock += 1
            else:
                get_col_king += 1
                get_row_king += 1

        if move == 'LB' and get_col_king - 1 >= 0 and get_row_king + 1 <= 7:
            if get_col_king - 1 == get_col_rock and get_row_king + 1 == get_row_rock:
                if get_col_rock - 1 >= 0 and get_row_rock + 1 <= 7:
                    get_col_king -= 1
                    get_row_king += 1
                    get_col_rock -= 1
                    get_row_rock += 1
            else:
                get_col_king -= 1
                get_row_king += 1
        

reverse_king_y = next(k for k,v in y.items() if v== get_col_king)
reverse_rock_y = next(k for k ,v in y.items() if v== get_col_rock)

print(str(reverse_king_y)+str(8-get_row_king))  
print(str(reverse_rock_y)+str(8-get_row_rock))

