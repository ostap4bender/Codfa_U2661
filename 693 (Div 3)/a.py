def get_cut(a):
    c = 1
    while a % 2 == 0:
        a /= 2
        c *= 2
    return c


for _ in range(int(input())):
    w, h, n = map(int, input().split())
    w_c, h_c = map(get_cut, (w, h))
    # print(w_c, h_c)
    print('NO') if w_c * h_c < n else print('YES')
