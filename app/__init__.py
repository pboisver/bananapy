from flask import Flask

from app.foo import bar

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World!'


app.add_url_rule('/foo', None, bar)

if __name__ == '__main__':
    app.run()
