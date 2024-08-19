"""
짝수 층 : 왼쪽에서 끝남
홀수 층 : 오른쪽에서 끝


i 가 짝수냐 홀수냐
"""

X = int(input())
i, total = 0, 0
while X > total:
    i += 1
    total += i
dev = total - X

if i%2 == 0:
    print(f"{i-dev}/{1+dev}")
else:
    print(f"{1+dev}/{i-dev}")

