while True:
    try:
        num = int(input('Enter an integer: '))
        break
    except ValueError:
        print('Try again.')
