#!/usr/bin/python3
'''
Flask Web Application

This script starts a simple Flask web application with several routes:
- The root route returns a greeting.
- The '/hbnb' route returns 'HBNB'.
- The '/c/<text>' route returns 'C' followed by a user-provided text.

Dependencies:
- Flask
'''

from flask import Flask, escape
app = Flask(__name__)


@app.route('/')
def hello():
    '''
    Hello route that returns a greeting.

    Returns:
    str: A greeting message.
    '''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''
    HBNB route that returns 'HBNB'.

    Returns:
    str: The string 'HBNB'.
    '''
    return 'HBNB:'


@app.route('/c/<text>')
def c_text(text):
    '''
    Displays 'C' followed by the value of <text>.

    Parameters:
    text (str): The text to be displayed, underscores will be replaced with spaces.

    Returns:
    str: A string formatted as 'C <text>'.
    '''
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    app.url_map.strict_slashes = False
