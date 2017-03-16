while True:
    user_input = input('Enter text: ')
    if user_input.upper() == 'Q':
        break

for n in range(1, 51):

    if n % 3 == 0:
        continue

    print(n)
