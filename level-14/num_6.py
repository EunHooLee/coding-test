import sys

sys.stdin = open('input.txt','r')

N, M = map(int, sys.stdin.readline().split())

people = []
for _ in range(N):
    people.append(sys.stdin.readline().rstrip())
people = set(people)

ans = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in people:
        ans.append(name)

print(len(ans))
for name in sorted(ans):
    print(name)