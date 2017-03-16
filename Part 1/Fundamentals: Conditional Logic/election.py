from random import random

count = 10000


def regional_votes(probability_a):
    results = 0

    for i in range(0, count):
        result = random() * 100
        results += result

    print("Candidat A: ", results / count * probability_a / 100)
    print("Candidat B: ", results / count * (100 - probability_a) / 100)
    print("---")


regional_votes(87)
regional_votes(65)
regional_votes(17)
