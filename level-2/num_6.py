a, b = map(int, input().split())
c = int(input())

k = a * 60 + b + c

print(k//60%24,k%60)