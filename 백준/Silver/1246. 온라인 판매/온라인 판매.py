import sys

N,M = map(int,sys.stdin.readline().split())

wanted_price = []
for  _ in range (M) :
    temp = int(sys.stdin.readline().rstrip())
    wanted_price.append(temp)

wanted_price.sort()


can_by = 0
profits = []
for i in range(0,len(wanted_price)) :
    proposed = wanted_price[i]
    can_by = len(wanted_price)-i
    eggs_can_sold = min(can_by, N)
    egg_price_total = proposed * eggs_can_sold

    profits.append((proposed,egg_price_total))

profits.sort(reverse= True, key = lambda x : x[1])

print(profits[0][0], profits[0][1])