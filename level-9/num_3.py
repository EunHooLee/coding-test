while True:
    n = int(input())
    if n == -1:
        break
    
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    
    if sum(divisors) != n:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = ",end='')
        print(' + '.join(map(str,divisors)))

