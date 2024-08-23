import sys

sys.stdin = open('input.txt','r')

N, M = map(int, sys.stdin.readline().split())
S = []
for _ in range(N):
    S.append(sys.stdin.readline().rstrip())
S = set(S)

cnt = 0
for _ in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        cnt += 1
print(cnt)