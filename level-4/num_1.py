import sys

N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

ans = 0
for i in x:
    if i == v:
        ans +=1

print(ans)