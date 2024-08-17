import sys

sys.stdin = open("input.txt", "r")

row, col, val_max = 0, 0, 0
for i in range(9):
    row_i = list(map(int, input().split()))
    val_i_max = max(row_i)
    if val_i_max >= val_max:
        val_max = val_i_max
        row = i + 1
        col = row_i.index(val_i_max) + 1
print(val_max)
print(row, col)
