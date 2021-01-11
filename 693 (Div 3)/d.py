for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    prior = {'a': [0, 0] + sorted(list(filter(lambda x: x % 2 == 0, arr))),
             'b': [0, 0] + sorted(list(filter(lambda x: x % 2 == 1, arr)))}
    bank = {'a': 0,
            'b': 0}


    def move(author):
        me = 'a'
        op = 'b'
        if author == 2: me, op = op, me

        if prior[me][-1] > prior[op][-1] - prior[op][-2]:
            bank[me] += prior[me].pop()
        else: prior[op].pop()


    i = 0
    while len(prior['a']) != 2 or len(prior['b']) != 2:
        move(1+i)
        i = (i + 1) % 2
        # print(prior, bank, sep='\n')
    if bank['a'] > bank['b']:
        print('Alice')
    elif bank['a'] < bank['b']:
        print('Bob')
    else:
        print('Tie')





