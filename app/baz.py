import logging
from flask import Flask
from app.foo import bar

# If app is started directly via 'python -m app.__init__`
logging.warning('from app.baz.py')

bong = Flask(__name__)


@bong.route('/')
def hello_world() -> str:
    return 'Hello World!'


bong.add_url_rule('/foo', None, bar)

# If app is started as __main__ (e.g. from  'python -m app.__init__`
if __name__ == '__main__':
    logging.warning('from __name__ == __main__ in app.baz.py')
    bong.run()
