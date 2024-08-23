import sys

sys.stdin = open('input.txt','r')
cnt = [0] * 10001
for _ in range(int(sys.stdin.readline())):
    cnt[int(sys.stdin.readline())] += 1

for num, c in enumerate(cnt):
    for _ in range(c):
        print(num)