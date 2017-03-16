from capitals import capitals_dict

from random import randint


def choose_capital(capitals_dict):
    capitals_count = len(capitals_dict)

    states = list(capitals_dict.keys())
    chosen_index = int(randint(0, capitals_count - 1))
    state = states[chosen_index]

    return capitals_dict[state]


while True:
    chosen_capital = choose_capital(capitals_dict).lower()
    print(chosen_capital)
    user_capital = input('What is the capital of {}? '.format(chosen_capital)).lower().strip()

    if user_capital == chosen_capital:
        print('Correct!')
        break
    elif user_capital == 'exit':
        print('Goodbye')
        break
    else:
        continue
