# 나눌수있으면 계속 나눠라
# 못나눌때까지
# 재귀

def division(x):
    
    for i in range(2,x):
        if x % i == 0:
            return [i] + division(x//i)
    
    return [x] # 안나눠지면 그 값 반환

def main():
    N = int(input())
    if N != 1:
        prime_factors = division(N)
        for p in sorted(prime_factors):
            print(p)
    
main()