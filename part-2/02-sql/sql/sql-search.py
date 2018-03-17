import sqlite3

allowed_operations = ['max', 'min', 'avg', 'sum', 'exit']

with sqlite3.connect('newnumb.db') as conn:
    c = conn.cursor()

    while True:
        operation = input('What to do? ')

        if operation == 'exit':
            break

        elif operation in allowed_operations:
            c.execute('SELECT {0} (num) from nums'.format(operation))
            result = c.fetchone()
            print(result)

        else:
            print(
                'Please, use one of these operations: {0}.'.format(
                    ', '.join(allowed_operations)
                    )
                )

