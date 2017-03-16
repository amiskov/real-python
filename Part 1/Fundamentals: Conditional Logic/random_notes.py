from random import randint

print(randint(2, 10))  # random number from 2 to 10 including 2 and 10

heads = 0
tails = 0

for trial in range(0, 10000):
    while randint(0, 1) == 0:
        tails += 1
    heads += 1

print("heads/tails: ", heads / tails)


def toss_die():
    return randint(1, 6)


print(toss_die())

sum_tosses = 0
for toss in range(1, 10000):
    sum_tosses += toss_die()

print(sum_tosses / 10000)
