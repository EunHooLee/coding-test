"""
1 layer = 1 : 1개        - 1 <= N < 2
2 layer = 2 ~ 7 : 6개    - 2 <= N < 8
3 layer = 8 ~ 19 : 12 개 - 8 <= N < 20 
4 layer = 20 ~ 37 : 18 개
5 layer = 38 ~ 61 : 24 개

6 * (num_layer - 1) = layer 개수

0 : 1
1 : 1 + 1
2 : 1 + 1 + 6*1


"""

N = int(input())
i, lower = 0, 1

while True:
    i += 1
    if i != 1:
        upper = lower + 6*(i-1)
    else:
        upper = lower + 1
    
    if lower <= N < upper:
        print(i)
        break
    lower = upper



