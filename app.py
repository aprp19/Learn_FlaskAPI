from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def penjumlahan():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    hasil = a + b
    response = {
        "result": hasil
    }

    return response


@app.route('/multiply', methods=['PUT'])
def multiply():
    a = int(request.headers['a'])
    b = int(request.headers['b'])
    hasil = a * b
    response = {
        "result": hasil
    }

    return response


def calculation(a, b, operator):
    hasil = 0

    if operator == "+":
        hasil = a + b
    if operator == "-":
        hasil = a - b
    if operator == "*":
        hasil = a * b
    if operator == "/":
        hasil = a / b

    return hasil


@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_json()
    a = int(data['a'])
    b = int(data['b'])
    operator = data['operator']
    result = calculation(a, b, operator)

    response = {
        "result": result
    }

    return response


@app.route('/path/<operator>', methods=['GET'])
def path_calculator(operator):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = calculation(a, b, operator)

    response = {
        "result": result
    }

    return response


# Authentication
def basic_auth_required(func):
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_basic_auth(auth.username, auth.password):
            return authenticate()
        return func(*args, **kwargs)

    return decorated


def check_basic_auth(username, password):
    # Perform your authentication logic here
    # You can check the credentials against a database, file, or any other method
    # Return True if the credentials are valid, False otherwise
    # Example:
    valid_username = 'admin'
    valid_password = 'password'
    return username == valid_username and password == valid_password


def authenticate():
    response = {
        "Message": "Authentication Required"
    }

    return response


@app.route('/protected')
@basic_auth_required
def protected_route():
    response = {
        "Message": "Authentication Successfully"
    }

    return response


if __name__ == '__main__':
    app.run()
