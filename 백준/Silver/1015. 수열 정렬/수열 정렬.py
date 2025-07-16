N = int(input())
A = list(map(int, input().split()))

indexed = list(enumerate(A)) 
indexed.sort(key=lambda x: (x[1], x[0]))  

P = [0] * N
for idx, (original_idx, _) in enumerate(indexed):
    P[original_idx] = idx

print(*P)
