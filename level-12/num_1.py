import sys

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())

cards = sorted(map(int, input().split()))
card_sum = 0

for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for k in range(j+1,len(cards)):
            temp = cards[i] + cards[j] + cards[k]
            if temp > card_sum and temp <= M:
                card_sum = temp

print(card_sum)

