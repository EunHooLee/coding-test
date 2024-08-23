import sys

sys.stdin = open('input.txt','r')

N, M = map(int,sys.stdin.readline().split())
poketmon = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    poketmon[name] = str(i+1)
    poketmon[str(i+1)] = name

for _ in range(M):
    print(poketmon[sys.stdin.readline().rstrip()])