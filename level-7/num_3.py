import sys

sys.stdin = open("input.txt","r")

matrix = []*5
col_max_len = 0

ans = ""
for _ in range(5):
    row_i = list(sys.stdin.readline().rstrip())
    matrix.append(row_i)
    if len(row_i) > col_max_len:
        col_max_len = len(row_i)

for j in range(col_max_len):
    for i in range(5):
        try:
            ans += matrix[i][j]
        except IndexError:
            continue
print(ans)