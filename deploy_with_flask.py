from flask import Flask
from flask import request
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/add')
def add():
    first_value = float(request.args.get('first_value', ''))
    second_value = float(request.args.get('second_value', ''))
    return str(first_value + second_value)

@app.route('/stocks')
def stocks():
    random_value = random.random()
    if(random_value> 0.5):
        return 'Your stocks will go up today! :)'
    else:
        return 'Your stocks will go down today :('

if __name__ == '__main__':
    app.run()
