import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

ans = []
for i in A:
    if i < X:
        ans.append(i)

print(*ans)