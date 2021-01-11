for _ in range(int(input())):
    n = int(input())
    # candy = list(map(int, input().split()))
    one = two = 0
    f = False
    for c in input().split():
        c = int(c)
        if c == 2:
            two = (two + 1) % 2
        if c == 1:
            f = True
            one = (one + 1) % 4
    print('YES') if (two == 1 and one % 2 == 0 and f) or (two == 0 and one % 2 == 0) else print('NO')

