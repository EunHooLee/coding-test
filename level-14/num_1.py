import sys

sys.stdin = open('input.txt','r')
N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
label = list(map(int, sys.stdin.readline().split()))

for i in label:
    print(int(i in cards),end=' ')