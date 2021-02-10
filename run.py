# Run a test server.
import logging

from app import baz

import os

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)


logging.info('Starting from app.baz.py')

baz.bong.run(debug=True)