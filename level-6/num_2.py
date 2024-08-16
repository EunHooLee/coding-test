num_piece = list(map(int, input().split()))
pivot = [1, 1, 2, 2, 2, 8]

for i in range(len(num_piece)):
    pivot[i] -= num_piece[i]
print(*pivot)