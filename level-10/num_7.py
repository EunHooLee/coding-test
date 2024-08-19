while True:
    edges = sorted(map(int, input().split()))
    if edges[0] == 0:
        break
    
    if edges[0] + edges[1] <= edges[2]:
        print('Invalid')
    else:
        if len(set(edges)) == 1:
            print('Equilateral')
        elif len(set(edges)) == 2:
            print('Isosceles')
        else:
            print('Scalene')