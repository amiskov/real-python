# Flask: Quick Start
Установка пакетов в виртуальном окружении глючит, когда в пути есть пробелы.

https://github.com/mjhea0/thinkful-mentor/tree/master/python/main_routine

Подробнее про декораторы в Питоне:
- [Primer on Python Decorators](https://realpython.com/blog/python/primer-on-python-decorators/)
- [Understanding Python Decorators in 12 Easy Steps!](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)

Фласк сам пытается угадать [код ответа](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). Но в REST API принято их указывать руками, потому что фронт от кодов зависит.

Включить сообщения об ошибках прямо в браузере и автоперезапускать серврер можно, указав в коде:

```python
app.config['DEBUG'] = True
```

