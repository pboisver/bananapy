# what do you want to do when `FLASK_APP=app flask run` loads the package `app`
import logging
from app.baz import bong

logging.warning('from app.__init__')

if __name__ == '__main__':
    logging.warning('Starting from __name__ == __main__ in app.__init__')
    bong.run()
