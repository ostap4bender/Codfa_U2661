for _ in range(int(input())):
    n = int(input())
    up = 0
    down = 0
    ss = 0
    in_a_row_3 = [False, False]
    is_3 = False

    arr = list(map(int, input().split()))

    def do():
        if in_a_row_3[0]:
            if in_a_row_3[1]:
                return True
            else:
                in_a_row_3[1] = True
                return False
        else:
            in_a_row_3[0] = True
            return False

    for i in range(1, n-1):
        # print('ii', i, arr[i])
        if arr[i-1] < arr[i] > arr[i+1]:
            ss += 1
            is_3 = True if do() else is_3

        elif arr[i-1] > arr[i] < arr[i+1]:
            ss += 1
            do()
            is_3 = True if do() else is_3

        else:
            in_a_row_3[0], in_a_row_3[1] = False, in_a_row_3[0]

    if is_3:
        print(ss-3)
    else:
        print(max(0, ss-1))





