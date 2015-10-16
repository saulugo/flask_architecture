#Flask Applications Architecture

A Flask App is structured the following way:

1) **Application Instance:** All Flask applications must create an application instance. The web server
passes all requests it receives from clients to this object for handling using a protocol called 
Web Server Gateway Interface (WSGI)

The **app instance is** an object of the Class Flask. It is usually created as follow:

```python
from flask import Flask
app = Flask(__name__)
```

2)**Routes and View Functions:** the client sends requests to the web server, who in turn sends them to
the **app instance**. The app instance keeps a map of URLs (received from the web server - clients requests)
and Python functions to be run for each URL. This association between a URL and a Python function is
called a **Route**.

The Flask class has a decorator named **app.route**. This decorator is exposed by the **app instance**.
Each **route** is defined in Flask using this decorator **app.route**.

Each route is declared as follow, using the app.route decoratore exposed by the application instance:

```python
@app.route('/')
def index():
	return "<h1>Hello world!</h1>
```
The return of this function is called **the response** and it will be passed through the web server to the
client browser.

The functions of each routes are called **view functions**.

When the URL has a variable part, for example you want a page in your app to be called by the user's username,
you must use the following syntax in the route decorator:

```python
@app.route('/user/<username>)
def user(name):
	return '<h1>Hello, %s!</h1>' % name
```
The the URL match the fix portion will call the view function (user(name)) and send the URL part enclosed in the angle
brackets as a argument of the view function.

Also, the dynamic part of the URL, supports type definition. For example the route */user/<int:id>* will accept
only integers as the id.

Flask supports *int, float* and *path* class for the routes. The *path* type is a string but does not 
take the slashes as separators but as part of the dynamic content.

3)**Server Startup:** the application instance has the *run* method that launches 
Flask's integrated development web server.

```python
if __name__ = '__main__'
	app.run(debug=True)
```
