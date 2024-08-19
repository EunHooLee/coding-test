"""
1 : 2 ~ n
2 : 3 ~ n
3 : 4 ~ n

n-1 : n ~ n

(n-1)*(n-i)
"""
n = int(input())
sum = 0
for i in range(1,n):
    sum += (n-i)
print(sum)
print(2)