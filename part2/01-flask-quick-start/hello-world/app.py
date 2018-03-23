from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

# Динамический роут
@app.route('/search/<search_query>')
def search(search_query):
    return 'You search: ' + search_query

# Можно задавать тип параметру
@app.route('/integer/<int:value>')
def int_type(value):
    print(1 + value)
    return 'correct'

@app.route('/float/<float:value>')
def float_type(value):
    print(1 + value)
    return 'correct'

@app.route('/path/<path:value>') # строка со слешами сохранится в переменную
def path_type(value):
    print(value)
    return 'correct'

@app.route('/name/<name>') # строка со слешами сохранится в переменную
def index(name):
    if name.lower() == 'michael':
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404



# Если запустили этот файл напрямую из командной строки, а не импортировали где-то в другом файле:
# https://github.com/mjhea0/thinkful-mentor/tree/master/python/main_routine
if __name__ == '__main__':
    app.run()

