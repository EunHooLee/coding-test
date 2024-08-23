import sys

sys.stdin = open('input.txt','r')

coordinates = []
for _ in range(int(sys.stdin.readline())):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

coordinates.sort(key=lambda x: (x[1],x[0]))
for c in coordinates:
    print(c[0],c[1])