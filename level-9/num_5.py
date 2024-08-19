M = int(input())
N = int(input())

prime_numbers=[]

for num in range(M,N+1):
    if num == 1:
        continue
    
    prime = 1
    for i in range(2,num):
        if num%i == 0:
            prime = 0
            break
    
    if prime:
        prime_numbers.append(num)

if prime_numbers:
    print(sum(prime_numbers))
    print(min(prime_numbers))
else:
    print(-1)

