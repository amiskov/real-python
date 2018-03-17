from random import randint

trials = 10000
flips = 0

for toss in range(0, trials):
    heads = 0
    tails = 0

    # Keep tossing till both tails and heads will be at least 1:
    while heads == 0 or tails == 0:
        flips += 1

        if randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1

            # print heads, tails

print(flips / trials)
