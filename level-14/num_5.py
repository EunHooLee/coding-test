import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline())
cards_list = list(sys.stdin.readline().split())
cards_set = set(cards_list)

cards_dict = {}
for card in cards_set:
    cards_dict[card] = 0
for card in cards_list:
    cards_dict[card] += 1

M = int(sys.stdin.readline())
label = list(sys.stdin.readline().split())
for num in label:
    if num in cards_set:
        print(cards_dict[num],end=' ')
    else:
        print(0, end=' ')