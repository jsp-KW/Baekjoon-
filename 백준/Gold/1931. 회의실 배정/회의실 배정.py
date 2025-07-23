import sys

N = int(sys.stdin.readline())

meetings = []

for _ in range (N):
    start,end  = map (int, sys.stdin.readline().split())
    meetings.append((start,end))

meetings.sort(key=lambda x : (x[1], x[0]))


cnt = 0
end_time =0
for m_start, m_end  in meetings :
    if m_start >= end_time :
        cnt +=1
        end_time = m_end

print(cnt)