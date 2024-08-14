h, m = map(int, input().split())
k = h * 60 + m - 45

if k < 0:
    print((k+60*24)//60,(k+60*24)%60)
else:
    print(k//60,k%60)