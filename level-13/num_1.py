import sys

sys.stdin = open('input.txt','r')
arr = []
for _ in range(int(input())):
    num = int(input())
    arr.append(num)
for i in sorted(arr):
    print(i)