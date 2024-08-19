bars = sorted(map(int, input().split()))

k = bars[0] + bars[1] - bars[2]

if k > 0:
    print(sum(bars))
else:
    print(sum(bars)+(k-1))