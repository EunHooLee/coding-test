coordinate = [[],[]]
for _ in range(3):
    x, y = map(int, input().split())
    coordinate[0].append(x)
    coordinate[1].append(y)

for x in set(coordinate[0]):
    if coordinate[0].count(x) == 1:
        print(x, end=" ")
for y in set(coordinate[1]):
    if coordinate[1].count(y) == 1:
        print(y)