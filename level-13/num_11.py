# index 함수는 O(N)
# index 에 O(1)로 접근 하려면 딕셔너리 사용 필요할듯

import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())
coordinates = list(map(int, sys.stdin.readline().split()))
coordinates_sorted = sorted(set(coordinates))

coordinates_dict = {}
for i in range(len(coordinates_sorted)):
    coordinates_dict[coordinates_sorted[i]] = i

for c in coordinates:
    print(coordinates_dict[c], end=" ") 
