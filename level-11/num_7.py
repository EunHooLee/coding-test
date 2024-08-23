a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# c-a1 = 0 일 때 a0 >0 이면 솔루션 없어야되는거 아닌가?
# 맞았네?, 풀이를 보면 위 경우가 and 앞에서 걸러진다.

if (c - a1) == 0 :
    if a0 <=0:
        print(1)
    else:
        print(0)

elif (c-a1) > 0:
    if n0 >= a0/(c-a1):
        print(1)
    else:
        print(0)
else:
    print(0)