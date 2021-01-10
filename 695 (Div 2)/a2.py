cycle = '0123456789'

for _ in range(int(input())):
    n = int(input())
    # for n in range(100):
    if n >= 3:
        n -= 3
        k = n // 10
        o = n % 10
        print('989' + k*cycle + cycle[:o])

    else:
        print('989'[:n])
