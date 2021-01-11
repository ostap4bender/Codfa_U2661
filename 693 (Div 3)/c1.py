for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = [0] * n
    for i in range(n-1, -1, -1):
        s_i = i
        e = arr[s_i]
        while e + s_i < n:
            s_i += arr[s_i]
            e += res[s_i]

        res[i] = e
    # print(res, max(res))
    print(max(res))
