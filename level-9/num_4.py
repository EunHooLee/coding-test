N = int(input())
arr = list(map(int,input().split()))

ans = 0
for i in arr:
    if i == 1:
        continue
    divisors = []
    for j in range(2,i):
        if i%j == 0:
            divisors.append(j)
    if len(divisors) == 0:
        ans += 1

print(ans)