import sys

# N개의 도시

N= int(sys.stdin.readline())
M= int(sys.stdin.readline())
graph = [[] for _ in range (N+1)]
first_city=1
for _ in range (N) :
    city_connected = list(map(int,sys.stdin.readline().split()))
    for idx,second_city in enumerate(city_connected) :
        if second_city ==1 and first_city!= idx+1:
            graph[first_city].append (idx+1)
         
    first_city +=1

trip_plan = list(map(int,sys.stdin.readline().split()))

visited = [False] *(N+1)

def dfs (start) :
    visited[start] = True
    for nxt in graph[start] :
        if not visited[nxt] :
            dfs(nxt)

            
dfs (trip_plan[0])



for p in trip_plan :
    if not visited[p] :
        print("NO")
        sys.exit(0)


print("YES")