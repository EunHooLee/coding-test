total_price = int(input())
n = int(input())

ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += a*b

if ans == total_price:
    print('Yes')
else:
    print('No')