# Project: Holberton School User Authentication Service 🛡️💻

## Table of Contents

- [Introduction](#introduction)
- [Setting Up Your Flask Application](#setting-up-your-flask-application)
- [API Routes Declaration](#api-routes-declaration)
- [Managing Cookies](#managing-cookies)
- [Handling Request Form Data](#handling-request-form-data)
- [Returning HTTP Status Codes](#returning-http-status-codes)
- [Conclusion](#conclusion)

## Introduction

Welcome to the Holberton School User Authentication Service project! 🎉 In this endeavor, we will build a robust user authentication system using Python's Flask framework. This system will include functionalities such as declaring API routes, managing user sessions with cookies, capturing user input through forms, and understanding the significance of various HTTP status codes in authentication processes. Let's dive into creating a secure and efficient authentication service!

## Setting Up Your Flask Application

Before we start, ensure you have Flask installed in your Python environment. You can install Flask using pip:

```bash
pip install Flask
```

Create a new Python file, e.g., `app.py`, and initialize your Flask app:

```python
from flask import Flask
app = Flask(__name__)
```

## API Routes Declaration

Declaring API routes in a Flask app is essential for defining the endpoints that clients will interact with. Use the `@app.route()` decorator to map your functions to URLs. For user authentication, we might have routes for login and logout:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login logic here
    return 'Login Page'

@app.route('/logout')
def logout():
    # Logout logic here
    return 'You have been logged out'
```

## Managing Cookies

Cookies are vital for managing user sessions in web applications. Flask provides straightforward methods to set and retrieve cookies:

- **Setting a cookie**: Use `response.set_cookie(key, value)` to add a cookie to the response object.

```python
from flask import make_response

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('Cookie is set')
    resp.set_cookie('user_id', '123')
    return resp
```

- **Retrieving a cookie**: Use `request.cookies.get(key)` to access a cookie value.

```python
from flask import request

@app.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get('user_id')
    return 'User ID: ' + user_id
```

## Handling Request Form Data

To handle form data in Flask, access the `request.form` object in your route. This is crucial for login forms where you need to process username and password:

```python
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Authentication logic here
    return 'Welcome, ' + username
```

## Returning HTTP Status Codes

HTTP status codes are pivotal in indicating the result of an HTTP request. Flask allows you to return various status codes by returning a tuple with the response and the status code:

```python
from flask import abort

@app.route('/login', methods=['POST'])
def login():
    if not valid_login:
        abort(401)  # Unauthorized access
    else:
        return 'Logged in successfully', 200
```

## Conclusion

Throughout this Holberton School project, we've developed a fundamental user authentication service, mastering the art of API route declaration, cookie management, form data processing, and the use of HTTP status codes. These components are essential in building secure and efficient web applications. Congratulations on enhancing your skills in web development and security! 🏆💡
