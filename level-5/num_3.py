import sys

T = int(sys.stdin.readline())
for _ in range(T):
    strings = sys.stdin.readline().rstrip()
    print(strings[0] + strings[-1])