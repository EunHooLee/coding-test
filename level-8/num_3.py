import sys

sys.stdin = open('input.txt','r')
coins = [25, 10, 5, 1]
for _ in range(int(input())):
    money = int(input())

    for coin in coins:
        print(money//coin, end=' ')
        money -= money//coin * coin
    print('')
