x, y, z = map(int, input().split())

if x == y == z:
    print(10000 + x * 1000)
elif x != y and x !=z and y != z:
    print(max(x,y,z) * 100)
else:
    if x == y or x == z:
        print(1000 + x*100)
    else:
        print(1000 + z*100)
