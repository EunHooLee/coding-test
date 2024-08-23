# 1백만

import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())

logs = {}
for _ in range(N):
    name, status = sys.stdin.readline().split()
    logs[name] = status

for name in sorted(logs, reverse=True):
    if logs[name] == 'enter':
        print(name)

