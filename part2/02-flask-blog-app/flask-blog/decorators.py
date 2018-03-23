def makebold(fn):
    def wrapper():
        return '<b>' + fn() + '</b>'
    return wrapper

@makebold
def hello():
    return 'Hello'

print(hello())