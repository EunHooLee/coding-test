"""
정사각형의 개수: 1 * 1 > 2*2 > 4 * 4 > 8 * 8 > ... >  2**(N-1) * 2**(N-1)
N 번째 사각형의 총 개수 = 2**2(N-1)
1 개당 추가하는 점 5개

1: 4 
2: 4 + 5 * 1
3: 9 + 5 * 4 - 

N: (N-1번째 점의 개수) + 5 * 2**2(N-1) - 

2
3 = 2 + 1 
5 = 3 + 2
9 = 5 + 4

"""
# 한 변에 총 점의 개수
dots = 2 

for i in range(int(input())):
    dots += (dots-1)

print(dots**2)