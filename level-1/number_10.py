import sys

x = int(sys.stdin.readline())
y = int(sys.stdin.readline())

print(x*(y%10), x*((y%100)//10), x*(y//100), x*y, sep='\n')