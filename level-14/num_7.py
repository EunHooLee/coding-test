import sys

sys.stdin = open('input.txt','r')

N, M = map(int,sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

C = A.difference(B)
D = B.difference(A)

print(len(C.union(D)))