import sys

val = 0
idx = 0
for i in range(9):
    x = int(sys.stdin.readline())
    if val < x:
        val = x
        idx = i+1
print(val)
print(idx)
