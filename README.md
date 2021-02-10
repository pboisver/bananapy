

### Create and activate a virtual environment
```bash
python3 -m venv path/to/venv # or `virtualenv path/to/venv`
source <path/to/venv>/bin/activate
```

A [virtual environment](https://exploreflask.com/en/latest/environment.html) will make the current system or specified version of `python` and `pip` available and allow packages to be installed non-globally. install with `pip3 install virtualenv`. If you want to drop the current virtual environment: `deactivate`. And you can switch to another env with using the commands above.

## Run from the terminal

### Using the `flask` application 
`app` is the package loaded by `flask run` which  `__init__`s the Flask app (`bong`) by importing module `baz.py` which has the magic words: `bong = Flask(__name__)`. If the Flask target is the package `app`, `__init__.py` runs, importing `baz` and conditionally calling `bong.run()` if it is the entry point (`__main__`) which will start the Flask app. 
```bash
# export FLASK_APP=app # if constant default is needed
# export FLASK_ENV=development # if you want debug and reload
FLASK_APP=app flask run
# python -m app.__init__ # Pretty much the python equivalent invocation

```

Also, you can run the `baz.py` module directly since it instantiates the Flask app (`bong`) and contains an identical conditional call to `bong.run()`. Wrapping `bong.run()` in a check to see if the module is the application entry keeps Flask from starting twice (which Flask rejects with a warning). 
```bash
FLASK_APP=app.baz flask run
# python -m app.baz # equivalent invocation of module `baz.py` without starting flask first, but warns that app.baz is loaded and executed out-of order. DON'T DO THIS
```

### Running with `gunicorn`
`gunicorn` is a `WSGI` compliant server, so it can run the Flask app `bong` we set up by invoking the package `app`. Other servers will work, too
```bash
gunicorn app:bong
```

Finally, we can start the Flask app with `run.py` in the root of the project. `run.py` imports the `app` package (which imports the `baz` module, same as `FLASK_APP=app flask run`) and calls `baz.bong.run()` explicitly. This entry point is appropriate for development, and sets `debug=true` for the Flask server.

```bash
python run.py
```
### Run tests from the terminal
```bash
python -m unittest discover -s tests
```


### To dos
- Set up as a package
- make `app` a module
- add a second module
- run Flask tests
- Run a separate thread for a 'heart beat'
- try a 'real' server
