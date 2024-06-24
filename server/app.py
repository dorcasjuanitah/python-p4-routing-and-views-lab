#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p>{parameter}</p>'

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter+1))
    return f'<pre>{numbers}<//pre>'

@app.route('/math/<int:num1>/<int:num2>/<operation>')
def math(operation, num1, num2):
    if operation == '+':
        result == num1 +num2

    elif operation == '-':
        result == num1 - num2

    elif operation == '*':
        result = num1 * num2

    elif operation == 'div':
        result = num1 / num2

    elif operation == '%':
        result = num1 % num2
    
    else:
        return 'Invalid Operation'
        
    return f'<p>{num1}{operation}{num2} = {result}</p>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
