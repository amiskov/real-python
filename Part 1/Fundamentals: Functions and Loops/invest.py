def invest(amount, rate, time):
    print('principal amount: ${}'.format(amount))
    print('annual rate of return: {}'.format(rate))

    for year in range(1, time + 1):
        amount += amount * rate
        print('year {}: ${}'.format(year, amount))

invest(100, .05, 8)
invest(2000, .025, 5)