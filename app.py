"""
CP1404 - Practical 10
Flask Web Framework
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello World:)</h1>"


@app.route('/greet')
# def greet():
#     return "Hello"

@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


@app.route('/f')
@app.route('/f/<celsius>')
def convert(celsius=""):
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return f"{celsius} celsius equals {fahrenheit} fahrenheit"


if __name__ == '__main__':
    app.run()
