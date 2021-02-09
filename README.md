

### Create and activate a virtual environment
```bash
python3 -m venv path/to/venv # or `virtualenv path/to/venv`
source <path/to/venv>/bin/activate
```

A [virtual environment](https://exploreflask.com/en/latest/environment.html) will make the current system or specified version of `python` and `pip` available and allow packages to be installed non-globally. install with `pip3 install virtualenv`. If you want to drop the current virtual environment: `deactivate`. And you can switch to another env with using the commands above.

### Run from the terminal
```bash
export FLASK_APP=app # or app.py
export FLASK_ENV=development
flask run
```


### Run tests from the terminal
```bash
python -m unittest discover -s tests
```

### To dos
Set up as a package
make `app` a module
add a second module
run Flask tests
Run a separate thread for a 'heart beat'
